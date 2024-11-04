from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('tela-principal/', views.tela_principal, name='tela-principal'),
    path('controle/', views.controle, name='controle'),
]
