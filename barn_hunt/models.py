from django.db import models


class Owner(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return '"' + self.full_name + '"<' + self.email + '>'

class Dog(models.Model):
    call_name = models.CharField(max_length=100)
    registered_name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    height_in_inches = models.IntegerField()
    bitch_in_season = models.BooleanField(default=False)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.call_name + ' (' + self.registered_name + ')'

class Address(models.Model):
    address_lines = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='United States')

    def __str__(self):
        return self.address_lines.replace('\n', ';')

class Event(models.Model):
    title = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title

class TrialClass(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Trial(models.Model):
    start_time_description = models.CharField(max_length=200)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    trial_class = models.ForeignKey(TrialClass, on_delete=models.CASCADE, null=True)

    def __str__(self):
        ret = str(self.event) + ':'
        if self.trial_class:
            ret += str(self.trial_class)
        ret += ' - ' + self.start_time_description

        return ret
