from rest_framework import serializers
from datetime import date
import re

class NomeValidator:
    def __call__(self, value):
        if not re.match(r'^[a-zA-Z ]*$', value):
            raise serializers.ValidationError("Nome deve conter apenas letras e espaços.")


class TelefoneValidator:
    def __call__(self, value):
        if not re.match(r'^\d{11}$', value):
            raise serializers.ValidationError("O número de telefone deve conter 11 dígitos.")


class DataNascimentoValidator:
    def __call__(self, value):
        idade = date.today().year - value.year - ((date.today().month, date.today().day) < (value.month, value.day))
        if idade < 1 or idade > 17:
            raise serializers.ValidationError("Idade deve estar entre 1  e 17 anos.")


class StatusValidator:
    def __call__(self, value):
        if value not in ['checkin', 'checkout']:
            raise serializers.ValidationError("Escolha um status válido: 'checkin' ou 'checkout'.")
        

class SalaValidator:
    def __call__(self, value):
        if value not in ['sala 1', 'sala 2', 'sala 3', 'teens', 'adolescentes']:
            raise serializers.ValidationError("Sala inválida! Escolha entre 'sala 1', 'sala 2', 'sala 3', 'teens' e 'adolescentes'.")


class ClassificacaoValidator:
    def __call__(self, value):
        if value not in ['membro', 'visitante', 'congregado']:
            raise serializers.ValidationError("Classificação inválida! Escolha entre 'membro', 'visitante' e 'congregado'.")
        
class UsernameValidator:
    def __call__(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Username deve ter ao menos 3 caracteres.")