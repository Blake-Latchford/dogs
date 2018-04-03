from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.encoding import escape_uri_path
from django.views import generic

from .models import Event
from .forms import DogRegistrationForm


class UpcomingEventsView(generic.ListView):
    model = Event

    def address_to_google_url(self, address):
        address_pattern = address.address_lines.replace('\n', ' ') + '+'
        address_pattern += address.city + '+'
        address_pattern += address.state + '+'
        address_pattern += address.zipcode + '+'
        address_pattern += address.country

        return "http://maps.google.com?daddr=" + \
            escape_uri_path(address_pattern)

    def get_queryset(self):
        pending_events = Event.objects.filter(end_time__gte=timezone.now())
        ordered_events = pending_events.order_by('-start_time')
        return ordered_events

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for event in context['event_list']:
            event.address_google_url = self.address_to_google_url(
                event.address)

        return context

class DogRegistrationView(generic.edit.CreateView):
    form_class = DogRegistrationForm
    template_name = 'barn_hunt/dog_registration.html'

    def get_success_url(self):
        return reverse_lazy('barn_hunt:upcoming_events')
