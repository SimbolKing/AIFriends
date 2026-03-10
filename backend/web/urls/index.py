from django.urls import path, include

from web.views.index import index

urlpatterns = [
    path('', index),
    path('api/user/account/', include('web.urls.user.account')),
]
