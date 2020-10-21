from django.contrib.auth.models import User
from django.db import models


class EnderecoEntrega(models.Model):
    cep = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    numero = models.CharField(max_length=5)


class DemandaPeca(models.Model):
    descricao = models.TextField()
    endereco_entrega = models.ForeignKey(EnderecoEntrega, on_delete=models.CASCADE, related_name='demanda_pecas')
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    anunciante = models.ForeignKey(User, on_delete=models.PROTECT, related_name='demanda_pecas')
    status_finalizacao = models.CharField(max_length=255)
