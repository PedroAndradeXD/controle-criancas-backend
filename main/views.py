from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .serializers import LoginUsuarioSerializer

@api_view(['POST'])
def login(request):
    serializer = LoginUsuarioSerializer(data=request)

    if serializer.is_valid():
        usuario = serializer.validate_data
        return Response({"status": "Login realizado com sucesso!"})

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def cadastro_usuario(request):
    username = request.data.get('nome')
    senha = request.data.get('senha')

    if not username or not senha:
        return Response({"erro": "nome e senha são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        usuario = User.objects.create(
            username=username,
            password=make_password(senha)
        )

        return Response({"status": "Usuário criado com sucesso."})

    except Exception as e:
        return Response({"erro": str(e)}, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['POST'])
def cadastro_crianca(request):
    # Lógica para cadastrar uma nova criança
    return Response({"status": "Cadastro realizado com sucesso"})

@api_view(['GET'])
def tela_principal(request):
    # Lógica para exibir dados da tela principal
    return Response({"status": "Bem-vindo à tela principal"})

@api_view(['GET'])
def controle(request):
    # Lógica para controle de crianças
    return Response({"status": "Controle realizado com sucesso"})
