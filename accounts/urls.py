from django.urls import path
from .views import UserInfoCreate

urlpatterns = [
    path('userinfo/', UserInfoCreate.as_view()),
]
