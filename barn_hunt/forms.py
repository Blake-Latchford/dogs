from django import forms

from .models import Dog, Owner

class DogRegistrationForm(forms.ModelForm):
    owner_full_name = forms.CharField(max_length=200)
    owner_email = forms.EmailField()

    class Meta:
        model = Dog
        fields = [
            'call_name',
            'registered_name',
            'breed',
            'height_in_inches',
            'bitch_in_season',
        ]
