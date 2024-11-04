from django.db import models
from uuid import uuid4
from datetime import date


class Usuario(models.Model):
    id_usuario = models.UUIDField(primary_key=True, default=uuid4)
    username_usuario = models.CharField(max_length=255)
    senha_usuario = models.CharField(max_length=255)

    def __str__(self):
        return self.username_usuario


class Controle(models.Model):
    ESCOLHA_STATUS = [
        ('checkin', 'Check-in'),
        ('checkout', 'Check-out'),
    ]

    id_checkin = models.UUIDField(primary_key=True, default=uuid4)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_horario_checkin = models.DateTimeField(auto_now_add=True)
    data_horario_checkout = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=ESCOLHA_STATUS, default='checkin')

    def __str__(self):
        return self.status


class Responsavel(models.Model):
    id_responsavel = models.UUIDField(primary_key=True, default=uuid4)
    nome = models.CharField(max_length=255)
    relacionamento_crianca = models.CharField(max_length=255)
    telefone_responsavel = models.CharField(max_length=11)

    def __str__(self):
        return self.nome


class Crianca(models.Model):
    ESCOLHA_CLASSIFICACAO = [
        ('membro', 'Membro'),
        ('visitante', 'Visitante'),
        ('congregado', 'Congregado'),
    ]

    ESCOLHA_SALA = [
        ('kids 1', 'Kids 1'),
        ('kids 2', 'Kids 2'),
        ('kids 3', 'Kids 3'),
        ('teens', 'Teens'),
        ('adolescentes', 'Adolescentes'),
    ]

    id_crianca = models.UUIDField(primary_key=True, default=uuid4)
    id_checkin = models.ForeignKey(Controle, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField(default=date(2000, 1, 1))
    classificacao = models.CharField(max_length=10, choices=ESCOLHA_CLASSIFICACAO)
    sala = models.CharField(max_length=12, choices=ESCOLHA_SALA)

    def __str__(self):
        return self.nome
    
    @property
    def idade(self):
        today = date.today()
        idade = today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))
        return idade
    

class CriancaResponsavel(models.Model):
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    crianca = models.ForeignKey(Crianca, on_delete=models.CASCADE)


class ControleResponsavel(models.Model):
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    checkin = models.ForeignKey(Controle, on_delete=models.CASCADE)



