from django.urls import path, include
from .views import UserInfoCreate

urlpatterns = [
    path('userinfo/', UserInfoCreate.as_view()),
    path("accounts/", include("django.contrib.auth.urls")),
]
