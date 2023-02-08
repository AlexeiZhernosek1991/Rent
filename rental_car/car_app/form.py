from django import forms
from .models import *


class AddOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'date_star', 'date_over', 'telefon_num']

