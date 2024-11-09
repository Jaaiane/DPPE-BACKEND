from rest_framework import serializers
from .models import Usuario

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'cpf', 'telefone', 
                  'data_nascimento', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Usuario(**validated_data)
        user.set_password(validated_data['password'])  # Criptografa a senha
        user.save()
        return user