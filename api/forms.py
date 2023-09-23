# dwitter/forms.py

from django import forms
from .models import *

class DweetForm(forms.ModelForm):
    class Meta:
        model = Hokimiyat
        exclude = ("user", )

