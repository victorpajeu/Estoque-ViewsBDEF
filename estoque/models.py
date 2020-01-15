from django.db import models
from django.contrib.auth.models import User
from core.models.

MOVEMENT = (
    ('i', 'input'),
    ('e', 'exit'),
)


class Estoque(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    nf = models.PositiveIntegerField('Nota Fiscal', null=True, blank=True)
    movement = models.CharField(max_length=1, choices=MOVEMENT)

    class Meta:
        ordering = ('-created')

    def __str__(self):
        return str(self.pk)
