from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer

@api_view(['POST'])
def registro(request):
    telefone = request.data.get('telefone')
    
    if not telefone:
        return Response({'ERRO':'Campos obrigatórios incompletos'}, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(telefone=telefone).exists():
        return Response({'ERRO':f'O telefone {telefone} já existe'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logar_usuario(request):
    username = request.data.get('username')
    senha = request.data.get('senha')

    usuario = authenticate(username=username, password=senha)#ele vai ver se o usuario existe de fato, se existe vai retornar o usuario, se não, ele não retorna nada

    if usuario:
        refresh = RefreshToken.for_user(usuario)
        return Response({
            'acesso': str(refresh.access_token),
            'refresh': str(refresh)
        }, status=status.HTTP_200_OK)
    else:
        return Response({'Erro': 'Usuário ou/e senha incorreto(s)'}, status=status.HTTP_401_UNAUTHORIZED)
