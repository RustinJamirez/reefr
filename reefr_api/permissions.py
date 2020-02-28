from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if user is editing their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id


class ShowOwnTank(permissions.BasePermission):
    """Allow users to view their own tank"""
    def has_object_permission(self, request, view, obj):
        """Check the user is trying to view own tank"""
        return obj.user_profile.id == request.user.id


class UpdateOwnTank(permissions.BasePermission):
    """Allow users to update their own status"""
    """Check the user is trying to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id


class UpdateOwnUserParameters(permissions.BasePermission):
    """Allow users to update their own parameters"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id


class UpdateAndViewOwnParameterMeasurements(permissions.BasePermission):
    """Allow users to make measurements for their own tank"""

    def has_object_permission(self, request, view, obj):
        return obj.user_profile.id == request.user.id


class UpdateAndViewOwnFish(permissions.BasePermission):
    """Allow users to view/update fish for their own tank"""

    def has_object_permission(self, request, view, obj):
        return obj.user_profile.id == request.user.id


class UpdateAndViewOwnEquipment(permissions.BasePermission):
    """Allow users to view/update equipment for their own tank"""

    def has_object_permission(self, request, view, obj):
        return obj.user_profile.id == request.user.id


class UpdateAndViewOwnImage(permissions.BasePermission):
    """Allow users to view/update their own image"""

    def has_object_permission(self, request, view, obj):
        return obj.user_profile.id == request.user.id
