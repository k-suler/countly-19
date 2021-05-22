import uuid
from django.db import models
from django.conf import settings
from django.db.models.fields import TimeField
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


class Store(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    maxNumberOfCustomers = models.PositiveIntegerField(default=0)
    current_number = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "{} - {}".format(self.id, self.name)


class Event(models.Model):
    number = models.IntegerField(default=0)
    store = models.ForeignKey(Store, related_name='events', on_delete=models.CASCADE)
    data_time = models.DateTimeField()

    def __str__(self):
        return "{} - {} : {}".format(self.id, self.number, self.score, self.player)
