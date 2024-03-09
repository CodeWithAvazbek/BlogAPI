from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # faqatgina kurish uchun ruxsat beriladi
        if request.method in permissions.SAFE_METHODS:
            return True
        # edit qilish uchun ruxsatnoma faqatgina post mualifiga beriladi
        return obj.author == request.user
