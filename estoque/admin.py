from django.contrib import admin
from .models import EstoqueItens


@admin.register(EstoqueItens)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'qtd',
        'sd',
        )
