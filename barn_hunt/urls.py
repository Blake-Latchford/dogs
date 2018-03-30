from django.urls import path

from . import views

app_name = 'barn_hunt'
urlpatterns = [
    path('', views.UpcomingEventsView.as_view(), name='upcoming_events'),
    path('<int:event_id>/register_dog', views.DogRegistrationView.as_view(), name='register_dog'),
]
