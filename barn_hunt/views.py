from django.utils import timezone
from django.views import generic

from .models import Event

class UpcomingEventsView(generic.ListView):
    model = Event

    def get_queryset(self):
        pending_events = Event.objects.filter(end_time__lte=timezone.now())
        ordered_events = pending_events.order_by('-start_time')
        return ordered_events
