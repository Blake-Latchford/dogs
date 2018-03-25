import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Owner

class OwnerTests(TestCase):
    def test_happy_path(self):
        owner = Owner(
            full_name='John Doe',
            email='john.doe@domain.com')
        self.assertIsInstance(owner, Owner)

    def test_valid_name_characters(self):
        valid_name_strings = (
            "O'Conor",
        )
        for name in valid_name_strings:
            with self.subTest(name=name):
                owner = Owner(
                    full_name=name,
                    email='john.doe@domain.com')
                self.assertIsInstance(owner, Owner)

