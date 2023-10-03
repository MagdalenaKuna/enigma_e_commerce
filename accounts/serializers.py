from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['user', 'role']

    def create(self, validated_data):
        return UserInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.role = validated_data.get('role', instance.role)
