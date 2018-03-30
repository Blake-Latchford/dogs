from django.test import TestCase

from . import forms

class DogRegistrationFormTests(TestCase):
    def test_empty_form(self):
        form = forms.DogRegistrationForm()
        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())

    def test_basic_valid_form(self):
        form = forms.DogRegistrationForm({
            'call_name': 'Meriln',
            'registered_name': 'Pi R Squared',
            'breed': 'Border Terrier',
            'height_in_inches': 7,
            'bitch_in_season': False,
        })
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())

    def test_incomplete_form(self):
        form = forms.DogRegistrationForm({
            'call_name': 'Meriln',
            'registered_name': 'Pi R Squared',
            'breed': 'Border Terrier',
            #'height_in_inches': 7,
            'bitch_in_season': False,
        })
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())
        self.assertIn('height_in_inches', form.errors)
