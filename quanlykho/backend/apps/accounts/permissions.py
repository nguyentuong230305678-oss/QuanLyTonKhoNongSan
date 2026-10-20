from rest_framework.permissions import BasePermission

def role_required(*roles):
    class RolePermission(BasePermission):
        def has_permission(self, request, view):
            u = request.user
            return bool(
                u and u.is_authenticated and
                (u.is_superuser or u.groups.filter(name__in=roles).exists())
            )
    return RolePermission