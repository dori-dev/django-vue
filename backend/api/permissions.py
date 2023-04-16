from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_superuser
        )


class IsItSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user and
            request.user == obj
        )


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            obj.author == request.user
        )


class IsStaffReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS and
            request.user and
            request.user.is_staff
        )
