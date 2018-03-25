from django.urls import path

from . import views

app_name = 'barn_hunt'
urlpatterns = [
    path('', views.UpcomingEventsView.as_view(), name='upcoming_events')
]
