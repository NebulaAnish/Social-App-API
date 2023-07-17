from rest_framework import permissions

# Permission to check post level privelages, if user can modify the post or read only
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request, view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

# Permission to check for current user
class IsOwner(permissions.BasePermission):
    def has_object_permission(self,request, view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user