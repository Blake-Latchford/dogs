from django.test import TestCase

from . import forms
from . import models

class DogRegistrationFormTests(TestCase):
    def test_empty(self):
        form = forms.DogRegistrationForm()
        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())

    def test_basic_valid(self):
        initial_owner_count = models.Owner.objects.count()
        form = forms.DogRegistrationForm({
            'owner_full_name': 'John Doe',
            'owner_email': 'john.doe@domain.com',
            'call_name': 'Meriln',
            'registered_name': 'Pi R Squared',
            'breed': 'Border Terrier',
            'height_in_inches': 7,
            'bitch_in_season': False,
        })

        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid(), form.errors.as_text())

        new_dog = form.save()

        self.assertIsInstance(new_dog, models.Dog)
        self.assertEqual(initial_owner_count + 1,
            models.Owner.objects.count())

    def test_incomplete(self):
        form = forms.DogRegistrationForm({
            'owner_full_name': 'John Doe',
            'owner_email': 'john.doe@domain.com',
            'call_name': 'Meriln',
            'registered_name': 'Pi R Squared',
            'breed': 'Border Terrier',
            #'height_in_inches': 7,
            'bitch_in_season': False,
        })

        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())
        self.assertIn('height_in_inches', form.errors)

        with self.assertRaises(ValueError):
            form.save()

    def test_existing_owner(self):
        owner = models.Owner.objects.create(
            full_name='John Doe',
            email='john.doe@domain.com',
        )
        initial_owner_count = models.Owner.objects.count()

        form = forms.DogRegistrationForm({
            'owner_id': owner.id,
            'call_name': 'Meriln',
            'registered_name': 'Pi R Squared',
            'breed': 'Border Terrier',
            'height_in_inches': 7,
            'bitch_in_season': False,
        })

        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid(), form.errors.as_text())

        new_dog = form.save()
        self.assertIsInstance(new_dog, models.Dog)
        self.assertEqual(initial_owner_count,
            models.Owner.objects.count())

    def test_unspecified_owner(self):
        form = forms.DogRegistrationForm({
            'call_name': 'Meriln',
            'registered_name': 'Pi R Squared',
            'breed': 'Border Terrier',
            'height_in_inches': 7,
            'bitch_in_season': False,
        })

        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())

        with self.assertRaises(ValueError):
            new_dog = form.save()
