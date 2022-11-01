from django import forms
from .models import *


class PaymentSystemMethod(forms.ModelForm):
    class Meta:
        model = PaymentModel
        fields = '__all__'
        
