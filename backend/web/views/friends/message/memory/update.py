from django.utils.timezone import now
from langchain_core.messages import SystemMessage, HumanMessage

from web.models.friend import SystemPrompt, Message
from web.views.friends.message.memory.graph import MemoryGraph


def create_system_message():
    system_prompts = SystemPrompt.objects.filter(title='memory').order_by('order_number')
    prompt = ''
    for sp in system_prompts:
        prompt += sp.prompt
    return SystemMessage(prompt)


def create_human_message(friend):
    prompt = f'[raw memory]\n{friend.memory}\n'
    prompt += f'[recent chat]\n'
    messages = list(Message.objects.filter(friend=friend).order_by('-id')[:10])
    messages.reverse()
    for m in messages:
        prompt += f'user: {m.user_message}\n'
        prompt += f'ai: {m.output}\n'
    return HumanMessage(prompt)


def update_memory(friend):
    app = MemoryGraph.create_app()

    inputs = {
        'messages': [
            create_system_message(),
            create_human_message(friend),
        ]
    }

    res = app.invoke(inputs)
    friend.memory = res['messages'][-1].content

    friend.update_time = now()
    friend.save()
