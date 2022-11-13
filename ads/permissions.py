from rest_framework.permissions import BasePermission

from ads.models import UserRoles


class IsOwnerSelection(BasePermission):
    message = "Вы не владелец этой подборки"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


class IsOwnerAdOrStaff(BasePermission):
    message = "Вы не владелец этого объявления, и не являетесь администратором"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author or request.user.role in [UserRoles.ADMIN, UserRoles.MODERATOR]:
            return True
        return False
