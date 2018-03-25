from django.db import models


class Owner(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()

class Dog(models.Model):
    call_name = models.CharField(max_length=100)
    registered_name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    height_in_inches = models.IntegerField()
    bitch_in_season = models.BooleanField(default=False)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

class Address(models.Model):
    address_lines = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='United States')

class Event(models.Model):
    title = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    start_time = models.DateField()
    end_time = models.DateField()

class TrialClass(models.Model):
    name = models.CharField(max_length=100)

class Trial(models.Model):
    start_time_description = models.CharField(max_length=200)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
