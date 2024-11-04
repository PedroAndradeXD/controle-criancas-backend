from django.contrib import admin
from .models import Usuario
admin.site.register(Usuario)

from django.contrib import admin
from .models import (Crianca, Responsavel, Controle)


@admin.register(Crianca)
class AdminCrianca(admin.ModelAdmin):
    list_display = ['nome',
                    'idade',
                    'classificacao',
                    'sala']
    search_fields = ['nome']

    readonly_fields = ['id_crianca']

    def get_fields(self, request, obj: None):
        fields = super().get_fields(request, obj)
        if obj is None:
            fields.remove('id_crianca')
        return fields


@admin.register(Responsavel)
class AdminResponsavel(admin.ModelAdmin):
    list_display = ['nome',
                    'relacionamento_crianca',
                    'telefone_responsavel']
    search_fields = ['nome']

    readonly_fields = ['id_responsavel']

    def get_fields(self, request, obj: None):
        fields = super().get_fields(request, obj)
        if obj is None:
            fields.remove('id_responsavel')
        return fields
    

@admin.register(Controle)
class AdminControle(admin.ModelAdmin):
    list_display = ['data_horario_checkin',
                    'data_horario_checkout',
                    'status']
    search_fields = ['id_checkin']

    def get_fields(self, request, obj: None):
        fields = super().get_fields(request, obj)
        if obj is None:
            fields.remove('id_checkin')
        return fields
