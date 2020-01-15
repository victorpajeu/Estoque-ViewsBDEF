from django.db import models


class Produto(models.Model):
    imported = models.BooleanField('Importação')
    name = models.CharField('Nome', max_length=100)
    ncm = models.CharField('NCM', max_length=8)
    price = models.DecimalField('Preço', max_digits=7, decimal_places=2)
    current_stock = models.IntegerField('Estoque atual')
    minimum_stock = models.PositiveIntegerField('Estoque Mínimo', default=0)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

