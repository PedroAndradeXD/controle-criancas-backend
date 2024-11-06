from rest_framework import serializers
from .models import Crianca, Responsavel, Controle

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
