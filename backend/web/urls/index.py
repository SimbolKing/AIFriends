from django.urls import path, include, re_path

from web.views.index import index

urlpatterns = [
    path('', index),
    path('api/user/account/', include('web.urls.user.account')),
    path('api/user/profile/', include('web.urls.user.profile')),
    re_path(r'^(?!media/|static/|assets/).*$', index)
]
