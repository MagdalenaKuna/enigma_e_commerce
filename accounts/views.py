from rest_framework import generics
from .models import UserInfo
from .serializers import UserInfoSerializer
from rest_framework import permissions


class UserInfoCreate(generics.CreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


class UserInfoUpdate(generics.UpdateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
