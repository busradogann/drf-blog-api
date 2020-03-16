from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        print("has_permission calisti")
        return request.user and request.user.is_authenticated

    message = "You must be the owner of this object."

    def has_object_permission(self, request, view, obj):
        print("has_object_permission calisti")
        return (obj.user == request.user) or request.user.is_superuser #is_staff sadece giris yapmis ve konu sahibine yetki verir, is_superuser ise tum yetkilere sahip kisidir.
