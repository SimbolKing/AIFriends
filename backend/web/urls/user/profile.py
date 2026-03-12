from django.urls import path

from web.views.user.profile.update import UpdateProfileView

urlpatterns = [
    path('update/', UpdateProfileView.as_view()),
]
