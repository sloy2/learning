from django import forms
from .models import *

class AddForm(forms.ModelForm):
    class Meta:
        model = info_table
        fields = ['username', 'email', 'number']