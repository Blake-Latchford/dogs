from django import forms

from .models import Registration

class RegisterForm(forms.ModelForm):
    model = Registration
