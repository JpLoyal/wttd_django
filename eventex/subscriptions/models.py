from django.db import models
from eventex.subscriptions.validators import validate_cpf


class Subscription(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11, validators=[validate_cpf])
    email = models.EmailField('email', blank=True)
    phone = models.CharField('telefone', max_length=20, blank=True)
    created_at = models.DateTimeField('created_at', auto_now_add=True)
    paid = models.BooleanField('pago', default=False)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

