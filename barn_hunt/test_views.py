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
        Event.objects.create(
            title='Upcoming Event',
            address=self.address,
            start_time=timezone.now() + datetime.timedelta(days=30),
            end_time=timezone.now() + datetime.timedelta(days=30,hours=1))

        response = self.get_response()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['event_list']), 1)

    def test_past_event(self):
        Event.objects.create(
            title='Past Event',
            address=self.address,
            start_time=timezone.now() - datetime.timedelta(days=30),
            end_time=timezone.now() - datetime.timedelta(days=29,hours=23))

        response = self.get_response()
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['event_list'])
