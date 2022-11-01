from django import forms
from .models import *


class LinksmediaForm(forms.ModelForm):
    class Meta:
        image = forms.FileField(required=False)
        model = Linksmedia
        exclude = ('user', 'profile')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mt-2 mb-2', 'placeholder': 'Enter Title'}),
            'url': forms.TextInput(attrs={'class': 'form-control mt-2 mb-2', 'placeholder': 'http://'}),
            'image': forms.FileInput(attrs={'type': 'hidden'})
        }
