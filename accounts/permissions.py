from rest_framework import permissions
from .models import UserInfo


def get_role(user):
    try:
        return UserInfo.objects.get(name='role').user_set.filter(id=user.id).exists()
    except ValueError:
        return None


class SalesmanPermission(permissions.BasePermission):
    def has_salesman_permission(self, request):
        role = get_role(request.user)
        return role == UserInfo.SALESMAN


class ClientPermission(permissions.BasePermission):
    def has_client_permission(self, request):
        role = get_role(request.user)
        return role == UserInfo.CLIENT
