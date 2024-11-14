from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Crianca, Responsavel, Controle
from .validators import UsernameValidator

class CriancaSerializer(serializers.ModelSerializer):
    idade = serializers.ReadOnlyField()

    class Meta:
        model = Crianca
        fields = ['id_crianca', 'nome', 'data_nascimento', 'classificacao', 'sala', 'idade']


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


class LoginUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(validators=[UsernameValidator()])
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def validate(self, data):
        username = data['username']
        password = data['password']

        try:
            user = User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            raise serializers.ValidationError("Usuário não existe.")
        
        if not user.check_password(password):
            raise serializers.ValidationError("Senha incorreta!")
        
        return user
    

class CadastroUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

        
