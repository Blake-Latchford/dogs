from django import forms

from .models import Dog

class DogRegistrationForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = [
            'call_name',
            'registered_name',
            'breed',
            'height_in_inches',
            'bitch_in_season',
        ]
