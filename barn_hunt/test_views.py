import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import Address, Event
from .views import UpcomingEventsView


class UpcomingEventsViewTests(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            address_lines='123 Fake St.\nBuilding A',
            city='Springfield',
            state='Missouri',
            zipcode='65800')

    def get_response(self):
        return self.client.get(reverse('barn_hunt:upcoming_events'))

    def test_upcoming_event(self):
        event = Event.objects.create(
            title='Upcoming Event',
            address=self.address,
            start_time=timezone.now() + datetime.timedelta(days=30),
            end_time=timezone.now() + datetime.timedelta(days=30, hours=1))

        response = self.get_response()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(response.context['event_list']),
            1, str(event.end_time))

    def test_past_event(self):
        Event.objects.create(
            title='Past Event',
            address=self.address,
            start_time=timezone.now() - datetime.timedelta(days=30),
            end_time=timezone.now() - datetime.timedelta(days=29, hours=23))

        response = self.get_response()
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['event_list'])

    def test_google_maps_url(self):
        view = UpcomingEventsView()
        maps_url = view.address_to_google_url(self.address)
        self.assertNotIn('\n', maps_url)
        self.assertNotIn(' ', maps_url)

class DogRegistrationTests(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            address_lines='123 Fake St.\nBuilding A',
            city='Springfield',
            state='Missouri',
            zipcode='65800')
        self.event = Event.objects.create(
            title='Upcoming Event',
            address=self.address,
            start_time=timezone.now() + datetime.timedelta(days=30),
            end_time=timezone.now() + datetime.timedelta(days=30, hours=1))

    def get_url(self):
        return reverse('barn_hunt:register_dog', kwargs={
            'event_id': self.event.id
        })

    def test_unbound_form(self):
        response = self.client.get(self.get_url())

        self.assertEqual(response.status_code, 200)

    def test_valid_bound_form(self):
        response = self.client.post(self.get_url(), {
            'owner_full_name': 'John Doe',
            'owner_email': 'john.doe@domain.com',
            'call_name': 'Merlin',
            'registered_name': 'Happy Hobbits, Pi R Squared',
            'breed': 'Border Terrier',
            'height_in_inches': 7,
            'bitch_in_season': False,
        })

        self.assertEqual(response.status_code, 302)

    def test_invalid_height(self):
        response = self.client.post(self.get_url(), {
            'owner_full_name': 'John Doe',
            'owner_email': 'john.doe@domain.com',
            'call_name': 'Merlin',
            'registered_name': 'Happy Hobbits, Pi R Squared',
            'breed': 'Border Terrier',
            'height_in_inches': 'Not a valid number!',
            'bitch_in_season': False,
        })

        self.assertEqual(response.status_code, 200)
