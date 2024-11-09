# auth_app/views.py

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token  # Importação do Token
from .models import Usuario  # Importando seu modelo personalizado
from .serializers import UserSerializer  # Importando o serializer

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = get_object_or_404(Usuario, username=username)  # Usando o modelo personalizado
    
    if not user.check_password(password):
        return Response({"error": "Credenciais inválidas"}, status=status.HTTP_404_NOT_FOUND)
    
    token, created = Token.objects.get_or_create(user=user)  # Criar ou obter o token
    serializer = UserSerializer(user)
    
    return Response({'token': token.key, 'user': serializer.data})

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.save()  # Salva o usuário usando o serializer
        token = Token.objects.create(user=user)  # Cria um token para o novo usuário
        
        return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")