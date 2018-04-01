from django import forms
from django.core.exceptions import ValidationError

from .models import Dog, Owner

class DogRegistrationForm(forms.ModelForm):
    owner_full_name = forms.CharField(
        max_length=200,
        required=False)
    owner_email = forms.EmailField(required=False)
    owner_id = forms.IntegerField(
        widget=forms.HiddenInput,
        required=False,
    )

    owner = forms.IntegerField(
        widget=forms.HiddenInput,
        required=False,
    )

    class Meta:
        model = Dog
        fields = [
            'call_name',
            'registered_name',
            'breed',
            'height_in_inches',
            'bitch_in_season',
            'owner',
        ]

    def clean(self):
        super().clean()

        owner = Owner.objects.filter(
            pk=self.cleaned_data.get('owner_id')).first()

        if not owner:
            owner = Owner.objects.filter(
                full_name=self.cleaned_data.get('owner_full_name'),
                email=self.cleaned_data.get('owner_email')).first()

        if not owner:
            if not self.cleaned_data.get('owner_full_name'):
                self.add_error('owner_full_name',
                    ValidationError('Field Required', code='required'))
            if not self.cleaned_data.get('owner_email'):
                self.add_error('owner_email',
                    ValidationError('Field Required', code='required'))

            if not self.errors:
                owner = Owner.objects.create(
                    full_name=self.cleaned_data.get('owner_full_name'),
                    email=self.cleaned_data.get('owner_email'))

        self.cleaned_data['owner'] = owner
        if owner:
            self.cleaned_data['owner_full_name'] = owner.full_name
            self.cleaned_data['owner_email'] = owner.email
