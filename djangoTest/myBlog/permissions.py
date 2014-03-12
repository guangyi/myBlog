'''
Created on Dec 18, 2013

@author: zhouguangyi2009
'''
from rest_framework import permissions

class isOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it
    """
    def has_object_permission(self, request,view, obj):
        # read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # write permissions are only allowed to the owner of the tip
        return obj.author == request.user