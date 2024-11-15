from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/user/', views.cadastro_user, name='cadastro-user'),
    path('cadastro/crianca/', views.cadastro_crianca, name='cadastro-crianca'),
    path('controle/<uuid:pk>/', views.CriancaCheckinCheckout.as_view(), name='controle'),
    path('criancas/', views.ListaCrianca.as_view(), name='lista-criancas'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
