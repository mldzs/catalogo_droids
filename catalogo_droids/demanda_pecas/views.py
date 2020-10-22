from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import DemandaPeca
from .serializers import DemandaPecaSerializer
from ..permissions import IsUsuarioAdministradorOuUsuarioDono
from ..util_views import MixedPermissionModelViewSet


class DemandaPecaViewSet(MixedPermissionModelViewSet):
    queryset = DemandaPeca.objects.all()
    serializer_class = DemandaPecaSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["descricao", "endereco_entrega__cep", "email", "anunciante__username"]
    search_fields = ["descricao", "endereco_entrega__cep", "email", "anunciante__username"]
    ordering_fields = ["descricao", "endereco_entrega__cep", "email", "anunciante__username"]

    http_method_names = ["get", "post", "put", "delete"]

    permission_classes_by_action = {
        "update": [IsAuthenticated, IsUsuarioAdministradorOuUsuarioDono],
        "destroy": [IsAuthenticated, IsUsuarioAdministradorOuUsuarioDono]
    }

    def get_queryset(self):
        todas_demanda_pecas = super().get_queryset()
        user = self.request.user

        if not user.is_superuser:
            todas_demanda_pecas = todas_demanda_pecas.filter(anunciante=user)

        return todas_demanda_pecas

    @action(methods=["PATCH"], detail=True, permission_classes=[IsAuthenticated, IsUsuarioAdministradorOuUsuarioDono])
    def finalizar_pedido(self, request, pk=None):
        demanda = self.get_object()
        demanda.finalizado = True
        demanda.save()

        return Response(data={"message": "Demanda finalizada com sucesso!"}, status=200)
