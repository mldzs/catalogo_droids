from django.contrib.auth.models import User
from rest_framework import serializers

from .models import EnderecoEntrega, DemandaPeca


class EnderecoEntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnderecoEntrega
        fields = "__all__"
        read_only_fields = ["id"]


class DemandaPecaSerializer(serializers.ModelSerializer):
    endereco_entrega = EnderecoEntregaSerializer()
    anunciante = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )

    class Meta:
        model = DemandaPeca
        fields = "__all__"

    def create(self, validated_data):
        endereco_entrega = validated_data.pop("endereco_entrega")
        obj_endereco_entrega = EnderecoEntrega.objects.create(**endereco_entrega)

        demanda_peca = DemandaPeca.objects.create(
            endereco_entrega=obj_endereco_entrega, **validated_data
        )
        return demanda_peca

    def update(self, instance, validated_data):
        endereco_entrega = validated_data.pop("endereco_entrega")
        obj_endereco_entrega, created = EnderecoEntrega.objects.get_or_create(
            **endereco_entrega
        )

        demanda_peca = DemandaPeca.objects.update(
            endereco_entrega=obj_endereco_entrega, **validated_data
        )
        return demanda_peca
