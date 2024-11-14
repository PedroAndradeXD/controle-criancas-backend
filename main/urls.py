from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro-crianca/', views.cadastro_crianca, name='cadastro-crianca'),
    path('cadastro-user/', views.cadastro_user, name='cadastro-user'),
    path('tela-principal/', views.tela_principal, name='tela-principal'),
    path('controle/', views.controle, name='controle'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
