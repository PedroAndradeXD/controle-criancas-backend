from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from datetime import datetime

from .models import Crianca, Controle
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status, generics
from .serializers import LoginUserSerializer, CadastroUserSerializer, CadastroCriancaSerializer, ListaCriancaSerializer, DetalheCriancaSerializer


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
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@permission_classes([AllowAny])
def cadastro_crianca(request):
    serializer = CadastroCriancaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"status": "Cadastro realizado com sucesso"}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([AllowAny])
class ListaCrianca(generics.ListAPIView):
    queryset = Crianca.objects.all()
    serializer_class = ListaCriancaSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome']


@permission_classes([AllowAny])
class CriancaCheckinCheckout(APIView):
    def get(self, request, pk):
        try:
            crianca = Crianca.objects.get(pk=pk)
            serializer = DetalheCriancaSerializer(crianca)
            return Response(serializer.data)
        except Crianca.DoesNotExist:
            return Response({"error": "Criança não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request, pk):
        try:
            crianca = Crianca.objects.get(pk=pk)
            #ultimo controle feito
            controle = Controle.objects.filter(id_usuario=crianca.id_crianca).last()

            #define novo status com base no último
            novo_status = 'checkout' if controle and controle.status == 'checkin' else 'checkin'

            #cria um novo registro de controle para o status atual
            Controle.objects.create(
                id_usuario=crianca,
                data_horario_checkin=datetime.now() if novo_status == 'checkin' else controle.data_horario_checkin,
                data_horario_checkout=datetime.now() if novo_status == 'checkout' else None,
                status=novo_status
            )
            return Response({"message": f"{novo_status.capitalize()} realizado com sucesso"})
        except Crianca.DoesNotExist:
            return Response({"error": "Criança não encontrada"}, status=status.HTTP_404_NOT_FOUND)

