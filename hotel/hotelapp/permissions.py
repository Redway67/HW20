from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False