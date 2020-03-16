from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        print("has_permission calisti")
        return request.user and request.user.is_authenticated

    message = "You must be the owner of this object."

    def has_object_permission(self, request, view, obj):
        print("has_object_permission calisti")
        return obj.user == request.user  #is_staff sadece giris yapmis konu sahibine yetki verir.
