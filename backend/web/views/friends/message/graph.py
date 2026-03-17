import os
from typing import TypedDict, Annotated, Sequence

import lancedb
from django.utils.timezone import localtime, now
from langchain_community.vectorstores import LanceDB
from langchain_core.messages import BaseMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.constants import START, END
from langgraph.graph import add_messages, StateGraph
from langgraph.prebuilt import ToolNode

from web.documents.utils.custom_embedding import CustomEmbeddings


class ChatGraph:
    @staticmethod
    def create_app():
        @tool
        def get_time() -> str:
            """Call this function if system wants to query exact time."""
            return localtime(now()).strftime('%Y-%m-%d')

        @tool
        def search_knowledge_base(query: str) -> str:
            """Call this function if user query information for AliCloud. Input: query Output: result"""
            db = lancedb.connect('./web/documents/lancedb_storage')
            embeddings = CustomEmbeddings()
            vector_db = LanceDB(
                connection=db,
                embedding=embeddings,
                table_name='my_knowledge_base',
            )
            docs = vector_db.similarity_search(query, k=3)
            context = '\n\n'.join([f'Content segment: {i + 1}\n{doc.page_content}' for i, doc in enumerate(docs)])
            return f'Find the information from knowledge base: \n\n{context}\n'

        tools = [get_time, search_knowledge_base]

        llm = ChatOpenAI(
            model='deepseek-v3.2',
            openai_api_key=os.getenv('API_KEY'),
            openai_api_base=os.getenv('API_BASE'),
            streaming=True,
            model_kwargs={
                "stream_options": {
                    "include_usage": True,
                }
            }
        ).bind_tools(tools)

        class AgentState(TypedDict):
            messages: Annotated[Sequence[BaseMessage], add_messages]

        def model_call(state: AgentState) -> AgentState:
            res = llm.invoke(state['messages'])
            return {'messages': [res]}

        def should_continue(state: AgentState) -> str:
            last_message = state['messages'][-1]
            if last_message.tool_calls:
                return "tools"
            return "end"

        tool_node = ToolNode(tools)

        graph = StateGraph(AgentState)
        graph.add_node('agent', model_call)
        graph.add_node('tools', tool_node)

        graph.add_edge(START, 'agent')
        graph.add_conditional_edges(
            'agent',
            should_continue,
            {
                'tools': 'tools',
                'end': END,
            }
        )
        graph.add_edge('tools', 'agent')

        return graph.compile()
