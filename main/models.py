from django.db import models
from uuid import uuid4
from datetime import date


class User(models.Model):
    id_user = models.UUIDField(primary_key=True, default=uuid4)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Controle(models.Model):
    ESCOLHA_STATUS = [
        ('checkin', 'Check-in'),
        ('checkout', 'Check-out'),
    ]

    id_checkin = models.UUIDField(primary_key=True, default=uuid4)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
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
    id_checkin = models.ForeignKey(Controle, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField(default=date(2000, 1, 1))
    classificacao = models.CharField(max_length=10, choices=ESCOLHA_CLASSIFICACAO)
    responsaveis = models.ManyToManyField(Responsavel, related_name="criancas")
    sala = models.CharField(max_length=12, choices=ESCOLHA_SALA)
    observacao = models.CharField(max_length=500, null=True)
    foto = models.ImageField(upload_to='fotos_criancas', null=True, blank=True)

    def __str__(self):
        return self.nome
    
    @property
    def idade(self):
        if not self.data_nascimento:
            return None
        today = date.today()
        idade = today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))
        return idade
    

class CriancaResponsavel(models.Model):
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    crianca = models.ForeignKey(Crianca, on_delete=models.CASCADE)


class ControleResponsavel(models.Model):
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    checkin = models.ForeignKey(Controle, on_delete=models.CASCADE)



