from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from eventex.subscriptions.models import Subscription


""" 
    !!! VALIDADORES ASSOCIADOS AO FORMULÁRIO PADRÃO (NÃO MODEL FORMS) !!!
    
def validate_cpf(value):
    # Remove caracteres não numéricos #
    cpf = ''.join(c for c in value if c.isdigit())

    if not value.isdigit():
        raise ValidationError(_('CPF inválido. Certifique-se de inserir apenas dígitos numéricos.'), 'digits')

    if len(cpf) != 11 or not cpf.isdigit():
        raise ValidationError(_('CPF inválido. Certifique-se de inserir exatamente 11 dígitos.'), 'length')
"""

"""
!!! FORMULÁRIO PADRÃO (SEM MODEL FORMS) !!!

class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', validators=[validate_cpf])
    email = forms.EmailField(label='Email', required=False)
    phone = forms.CharField(label='Telefone', required=False)

    def clean_name(self):
        nome_uncleaned = self.cleaned_data['name']
        partes = nome_uncleaned.split()
        nome_cleaned = ' '.join([part.capitalize() for part in partes])

        return nome_cleaned

    def clean(self):
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou telefone')

        return self.cleaned_data
"""

class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription
        fields = ['name', 'cpf', 'email', 'phone']


    def clean_name(self):
        nome_uncleaned = self.cleaned_data['name']
        partes = nome_uncleaned.split()
        nome_cleaned = ' '.join([part.capitalize() for part in partes])

        return nome_cleaned


    def clean(self):
        self.cleaned_data = super().clean()

        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou telefone')

        return self.cleaned_data