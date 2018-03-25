import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Owner, Dog, Address

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

    def test_string(self):
        owner = Owner(
            full_name='John Doe',
            email='john.doe@domain.com')
        self.assertIn( owner.full_name, str(owner) )


class DogTests(TestCase):
    def setUp(self):
        self.owner = Owner(
            full_name='John Doe',
            email='john.doe@domain.com')
        self.owner.save()
        self.dog = Dog(
            call_name='Merlin',
            registered_name='Pi R Squared, Happy Hobbits',
            breed='border terrier',
            height_in_inches=10,
            bitch_in_season=False,
            owner=self.owner)

    def test_happy_path(self):
        self.assertIsInstance(self.dog, Dog)

    def test_string(self):
        self.assertIn(self.dog.call_name, str(self.dog))
        

class AddressTests(TestCase):
    def setUp(self):
        self.address = Address(
            address_lines='123 Fake St.\nBuilding A',
            city='Springfield',
            state='Missouri',
            zipcode='65800')

    def test_address_happy_path(self):
        self.assertIsInstance(self.address, Address)

    def test_string(self):
        first_line = self.address.split('\n')[0]
        self.assertIn(first_line, str(self.address))

class EventTests(TestCase):
    def setUp(self):
        self.address = Address(
            address_lines='123 Fake St.\nBuilding A',
            city='Springfield',
            state='Missouri',
            zipcode='65800')
        self.address.save()

    def test_string(self):
        event = Event(
            title='Title',
            address=self.address,
            start_time=timezone.now(),
            end_time=timezone.now() )
        self.assertIn(event.title, str(event))

class TrialTests(TestCase):
    def setUp(self):
        self.address = Address(
            address_lines='123 Fake St.\nBuilding A',
            city='Springfield',
            state='Missouri',
            zipcode='65800')
        self.address.save()

        self.event = Event(
            title='Title',
            address=self.address,
            start_time=timezone.now(),
            end_time=timezone.now() )
        self.event.save()

        self.trial_class = TrialClass(name="Novice")
        self.trial_class.save()

        self.trial = Trial(
            start_time_description='Early Morning',
            event=self.event,
            trial_class=self.trial_class)

    def test_string(self):
        self.assertIn(trial.start_time_description, str(trial))

