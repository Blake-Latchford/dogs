import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Owner, Dog, Address, Event, Trial, TrialClass, CompetitionClass


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
        self.assertIn(owner.full_name, str(owner))


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
        first_line = self.address.address_lines.split('\n')[0]
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
            end_time=timezone.now())
        self.assertIn(event.title, str(event))


class TrialTests(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            address_lines='123 Fake St.\nBuilding A',
            city='Springfield',
            state='Missouri',
            zipcode='65800')

        self.event = Event.objects.create(
            title='Title',
            address=self.address,
            start_time=timezone.now(),
            end_time=timezone.now())

        self.competition_class = CompetitionClass.objects.create(
            name="Novice")

        self.trial = Trial.objects.create(
            time_description='Early Morning',
            event=self.event)

        self.trial_class = TrialClass.objects.create(
            competition_class=self.competition_class,
            trial=self.trial,
            price=0.0)

    def test_string(self):
        self.assertIn(self.trial.time_description, str(self.trial))

        trial_class_str = str(self.trial_class)
        self.assertIn(self.event.title, trial_class_str)
        self.assertIn(self.trial.time_description, trial_class_str)
