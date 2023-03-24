'''from datetime import timezone

from django.core.exceptions import ValidationError

from . models import reg
from django import forms
class Myform(forms.ModelForm):
    fname = forms.CharField(max_length=100, required=True)
    age = forms.IntegerField(required=True)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    email = forms.EmailField(required=True)'''


