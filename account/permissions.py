from rest_framework import permissions
from .models import Account


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Account):
            return obj == request.user
        return obj.account == request.user

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return request.user.is_authenticated


class IsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Account):
            return obj == request.user
        return obj.account == request.user

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_admin


