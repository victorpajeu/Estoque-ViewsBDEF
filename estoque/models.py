from django.db import models
from django.contrib.auth.models import User
from core.models import TimeStampedModel
from produto.models import Produto

MOVEMENT = (
    ('i', 'input'),
    ('e', 'exit'),
)


class Estoque(TimeStampedModel):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    nf = models.PositiveIntegerField('Nota Fiscal', null=True, blank=True)
    movement = models.CharField(max_length=1, choices=MOVEMENT)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.pk)


class EstoqueItens(models.Model):

    stock = models.ForeignKey(Estoque, on_delete=models.CASCADE)
    product = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtd = models.PositiveIntegerField()
    sd = models.PositiveIntegerField()

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.pk} - {self.stock.pk} - {self.product}'
