import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Owner, Dog

class OwnerTests(TestCase):
    def test_valid_name_characters(self):
        valid_name_strings = (
            "O'Conor",
        )
        for name in valid_name_strings:
            with self.subTest(name=name):
                owner = Owner(
                    full_name=name,
                    email='john.doe@domain.com')
                owner.save()
                self.assertIsInstance(owner, Owner)

class DogTests(TestCase):
    def test_happy_path(self):
        owner = Owner(
            full_name='John Doe',
            email='john.doe@domain.com')
        owner.save()
        dog = Dog(
            calll='Merlin',
            registered_name='Pi R Squared, Happy Hobbits',
            breed='border terrier',
            height_in_inches=10,
            bitch_in_season=False,
            owner=owner)
        dog.save()
        self.assertIsInstance(dog, Dog)

class AddressTests(TestCase):
    def address_happy_path(self):
        address = Address(
            address_lines='123 Fake St.\nBuilding A',
            city='Springfield',
            state='Missouri',
            zipcode='65800')
        address.save()
        self.assertIsInstance(address, Address)
