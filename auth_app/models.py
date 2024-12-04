from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15, blank=True)  # Campo para telefone
    endereco = models.TextField(blank=True)  # Campo para endereço
    data_nascimento = models.DateField(null=True, blank=True)  # Campo para data de nascimento
    nome_completo = models.CharField(max_length=255, blank=True)
    imagem_perfil = models.ImageField(upload_to='imagens_perfil/', null=True, blank=True)  # Campo para imagem de perfil

    def __str__(self):
        return self.get_full_name()  # Retorna o nome completo do usuário