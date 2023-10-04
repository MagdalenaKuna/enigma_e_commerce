from rest_framework import permissions
from .models import UserInfo


def get_role(user):
    try:
        userinfo = UserInfo.objects.get(user=user.id)
        return userinfo.role
    except ValueError:
        return None


class SalesmanPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        role = get_role(request.user)
        return role == UserInfo.SALESMAN


class ClientPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        role = get_role(request.user)
        return role == UserInfo.CLIENT
