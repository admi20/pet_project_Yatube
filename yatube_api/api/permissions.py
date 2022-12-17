from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    """
    Пользовательское разрешение: для пользователей - доступ к просмотру,
    для владельцев поста - доступ к
    редактированию и удалению.
    """
    def has_object_permission(self, request, view, obj):
        return (request.method in SAFE_METHODS
                or obj.author == request.user)
