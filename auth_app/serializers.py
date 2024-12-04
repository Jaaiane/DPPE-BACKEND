from rest_framework import serializers
from .models import Usuario  # Importar o novo modelo Usuario
from django.core.exceptions import ValidationError

class UsuarioSerializer(serializers.ModelSerializer):
    confirmar_senha = serializers.CharField(write_only=True)
    nome_completo = serializers.CharField(required=True)
    imagem_perfil = serializers.ImageField(required=False)  # Campo para imagem de perfil

    class Meta:
        model = Usuario
        fields = ['username', 'password', 'email', 'cpf', 'telefone', 'endereco', 'data_nascimento', 'confirmar_senha', 'nome_completo', 'imagem_perfil']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }

    def create(self, validated_data):
        if validated_data['password'] != validated_data.pop('confirmar_senha'):
            raise ValidationError({"confirmar_senha": "As senhas não coincidem."})

        usuario = Usuario(**validated_data)
        usuario.set_password(validated_data['password'])  # Armazena a senha de forma segura
        usuario.save()
        return usuario

    def validate_email(self, value):
        if " " in value:
            raise serializers.ValidationError("O email não pode conter espaços.")
        return value

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()