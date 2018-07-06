from django.forms import ModelForm, forms
from django.core.exceptions import NON_FIELD_ERRORS

from .models import Address


class AddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = '__all__'
