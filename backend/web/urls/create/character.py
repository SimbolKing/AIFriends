from django.urls import path

from web.views.create.character.create import CreateCharacterView
from web.views.create.character.get_list import GetListCharacterView
from web.views.create.character.get_single import GetSingleCharacterView
from web.views.create.character.remove import RemoveCharacterView
from web.views.create.character.update import UpdateCharacterView
from web.views.create.character.voice.get_list import GetVoiceList

urlpatterns = [
    path('create/', CreateCharacterView.as_view()),
    path('update/', UpdateCharacterView.as_view()),
    path('remove/', RemoveCharacterView.as_view()),
    path('get_single/', GetSingleCharacterView.as_view()),
    path('get_list/', GetListCharacterView.as_view()),
    path('voice/get_list/', GetVoiceList.as_view()),
]

