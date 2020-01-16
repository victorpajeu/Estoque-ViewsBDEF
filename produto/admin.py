from django.contrib import admin
from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'imported',
        'name',
        'ncm',
        'price',
        'current_stock',
        'minimum_stock',
    )
    search_fields = ('name',)
    list_filter = ('imported',)