from users.constants import Role
from rest_framework.permissions import BasePermission

from .models import Issue


class RoleIsSenior(BasePermission):

    def has_permission(self, request, api):
        return request.user.role == Role.SENIOR
            
    
    def has_object_permission(self, request, api, issue):
        return request.user.role == Role.SENIOR
    
class RoleIsJunior(BasePermission):

    def has_permission(self, request, api):
        return request.user.role == Role.JUNIOR
            
    
    def has_object_permission(self, request, api, issue):
        return request.user.role == Role.JUNIOR

class RoleIsAdmin(BasePermission):

    def has_permission(self, request, api):
        return request.user.role == Role.ADMIN
            
    
    def has_object_permission(self, request, api, issue):
        return request.user.role == Role.ADMIN

class IssueParticipant(BasePermission):

    def has_object_permission(self, request, api, issue: Issue):
        # if request.user == issue.junior or request.user == issue.senior:
        #     return True
        
        # return False
        return (request.user == issue.junior) or (request.user == issue.senior)
    