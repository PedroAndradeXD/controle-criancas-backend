from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .serializers import LoginUserSerializer, CadastroUserSerializer, CadastroCriancaSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    serializer = LoginUserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.validated_data
        return Response({"status": "Login realizado com sucesso!"}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def cadastro_user(request):
    username = request.data.get('username')

    if User.objects.filter(username=username).exists():
        return Response({"error": "Nome de usuário já cadastrado."}, status=status.HTTP_400_BAD_REQUEST)

    serializer = CadastroUserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "Usuário criado com sucesso!"}, status=status.HTTP_201_CREATED)
    return Response({serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@permission_classes([AllowAny])
def cadastro_crianca(request):
    serializer = CadastroCriancaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"status": "Cadastro realizado com sucesso"}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def tela_principal(request):
    # Lógica para exibir dados da tela principal
    return Response({"status": "Bem-vindo à tela principal"})

@api_view(['GET'])
def controle(request):
    # Lógica para controle de crianças
    return Response({"status": "Controle realizado com sucesso"})
