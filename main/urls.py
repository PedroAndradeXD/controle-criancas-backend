from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro-crianca/', views.cadastro_crianca, name='cadastro-crianca'),
    path('cadastro-usuario/', views.cadastro_usuario, name='cadastro-usuario'),
    path('tela-principal/', views.tela_principal, name='tela-principal'),
    path('controle/', views.controle, name='controle'),
]
