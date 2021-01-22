from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """ Grants permission to current signed in user"""
    def has_object_permission(self, request, view, obj):
        if request.methods in permissions.SAFE_METHODS:
            return True
        return obj.user == self.request.user


