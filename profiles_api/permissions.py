from rest_framework import permissions



class UpdateOwnProfile( permissions.BasePermission):
    """ Allows user to only edit their own profile """

    def has_object_permission(self, request,view,obj):
        """ check user is trying to edit their own profile """
        if request.method in permissions.SAFE_METHODS:
            return True
# OR if user is trying unsafe method like update or delete
        return obj.id==request.user.id
