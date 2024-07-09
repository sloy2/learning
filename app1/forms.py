from django import forms
from .models import *

class AddForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.CharField(max_length=20)
    number = forms.CharField(max_length=11)
    published = forms.BooleanField()