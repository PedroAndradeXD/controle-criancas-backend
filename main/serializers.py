from rest_framework import serializers
from .models import Crianca, Responsavel, Controle, Usuario
from .validators import UsernameValidator

class CriancaSerializer(serializers.ModelSerializer):
    idade = serializers.ReadOnlyField()

    class Meta:
        model = Crianca
        fields = ['id_crianca', 'nome', 'data_nascimento', 'classificacao', 'sala', 'idade']
        read_only_fields = ['id_crianca', 'idade'] 


class ResponsavelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Responsavel
        fields = ['id_responsavel', 'nome', 'relacionamento_crianca', 'telefone_responsavel']
        read_only_fields = ['id_responsavel']


class ControleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Controle
        fields = ['id_checkin', 'status', 'data_horario_checkin', 'data_horario_checkout']
        read_only_fields = ['id_checkin', 'status', 'data_horario_checkin', 'data_horario_checkout']

class LoginUsuarioSerializer(serializers.ModelSerializer):
    username = serializers.CharField(validators=[UsernameValidator()])
    senha = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['username', 'senha']

    def validate(self, data):
        username = data['username']
        senha = data['senha']

        try:
            usuario = Usuario.objects.get(username__iexact=username)
        except Usuario.DoesNotExist:
            raise serializers.ValidationError("Usuário não existe.")
        
        if not usuario.check_password(senha):
            raise serializers.ValidationError("Senha incorreta!")
        
        return usuario

        
