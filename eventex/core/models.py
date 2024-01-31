from django.db import models
from eventex.core.managers import EmailContactManager, PhoneContactManager


# Create your models here.

class Speaker(models.Model):
    name = models.CharField('nome', max_length=255)
    slug = models.SlugField('slug')
    description = models.TextField('descrição', blank=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Palestrante'
        verbose_name_plural = 'Palestrantes'

    def __str__(self):
        return self.name


class Contact(models.Model):
    objects = models.Manager()
    emails = EmailContactManager()
    phones = PhoneContactManager()

    EMAIL = 'E'
    PHONE = 'P'

    KINDS = (
        (EMAIL, 'Email'),
        (PHONE, 'Telefone'),
    )

    speaker = models.ForeignKey('Speaker', on_delete=models.CASCADE, verbose_name='Palestrante')
    kind = models.CharField('Tipo de Contato', max_length=1, choices=KINDS)
    value = models.CharField('Valor', max_length=255)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'


class Talk(models.Model):
    title = models.CharField('Título', max_length=200)
    start = models.TimeField('Início', blank=True, null=True)
    description = models.TextField('Descrição', blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name='Palestrante', blank=True)

    class Meta:
        verbose_name = 'Palestra'
        verbose_name_plural = 'Palestras'

    def __str__(self):
        return self.title
