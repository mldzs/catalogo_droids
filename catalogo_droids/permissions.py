from rest_framework.permissions import BasePermission


class IsUsuarioAdministrador(BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user.is_superuser


class IsUsuarioAnunciante(BasePermission):
    def has_permission(self, request, view) -> bool:
        return not request.user.is_superuser


class IsUsuarioAdministradorOuUsuarioDono(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.anunciante.is_superuser or obj.anunciante == request.user
