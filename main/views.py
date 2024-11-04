from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def login(request):
    # Lógica para autenticar o usuário
    return Response({'status': 'success', 'message': 'Login realizado com sucesso'})

@api_view(['POST'])
def cadastro(request):
    # Lógica para cadastrar uma nova criança
    return Response({'status': 'success', 'message': 'Cadastro realizado com sucesso'})

@api_view(['GET'])
def tela_principal(request):
    # Lógica para exibir dados da tela principal
    return Response({'status': 'success', 'message': 'Bem-vindo à tela principal'})

@api_view(['GET'])
def controle(request):
    # Lógica para controle de crianças
    return Response({'status': 'success', 'message': 'Controle realizado com sucesso'})
