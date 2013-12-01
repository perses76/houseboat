from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Port(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)

    def __unicode__(self):
        return self.name


class Boat(models.Model):
    port = models.ForeignKey(to=Port)
    owner = models.ForeignKey(to=User)
    name = models.CharField(max_length=100, unique=True, null=False)
    description = models.TextField(blank=True, null=False)
    photo = models.ForeignKey(to='BoatPhoto', null=True, related_name="main_photo", blank=True)
    size = models.CharField(max_length=100)  # size in the format {length}x{width}x{height} for ex.: 10000x20000x30000
    fuel = models.IntegerField(null=True)  # fuel consumption per 100 km???
    insurance = models.BooleanField()  # if boat has insurance
    generator = models.CharField(max_length=100, blank=True, null=False)

    def __unicode__(self):
        return self.name


class BoatPhoto(models.Model):
    boat = models.ForeignKey(to=Boat)
    photo = models.ImageField(upload_to='boat_photos')
    legend = models.CharField(max_length=100, blank=True, null=False)

    def __unicode__(self):
        return self.legend if self.legend else self.id


class BoatExtra(models.Model):
    boat = models.ForeignKey(to=Boat)
    name = models.CharField(max_length=100, blank=False, null=False)
    value = models.CharField(max_length=100, blank=True, null=False)

    def __unicode__(self):
        return self.name
