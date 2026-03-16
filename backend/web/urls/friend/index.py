from django.urls import path

from web.views.friends.get_list import GetListFriendView
from web.views.friends.get_or_create import GetOrCreateFriendView
from web.views.friends.message.chat import MessageChatView
from web.views.friends.message.get_history import GetHistoryView
from web.views.friends.remove import RemoveFriendView

urlpatterns = [
    path('get_or_create/', GetOrCreateFriendView.as_view()),
    path('remove/', RemoveFriendView.as_view()),
    path('get_list/', GetListFriendView.as_view()),
    path('message/chat/', MessageChatView.as_view()),
    path('message/get_history/', GetHistoryView.as_view())
]