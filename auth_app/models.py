from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)  # Torna o email único e obrigatório
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'usuarios'

    def __str__(self):
        return self.username