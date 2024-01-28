from rest_framework.permissions import BasePermission


class IsSuperuserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Allow read-only permissions for any request
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Check if the user is a superuser for other methods
        return request.user and request.user.is_superuser