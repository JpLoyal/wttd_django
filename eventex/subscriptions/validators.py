from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


def validate_cpf(value):
    # Remove caracteres não numéricos #
    cpf = ''.join(c for c in value if c.isdigit())

    if not value.isdigit():
        raise ValidationError(_('CPF inválido. Certifique-se de inserir apenas dígitos numéricos.'), 'digits')

    if len(cpf) != 11 or not cpf.isdigit():
        raise ValidationError(_('CPF inválido. Certifique-se de inserir exatamente 11 dígitos.'), 'length')
