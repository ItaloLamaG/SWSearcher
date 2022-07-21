from django.db import models
from .my_datetime import DateTimeModel
from .people import People


class Transport(DateTimeModel):
    """ Transportes """

    name = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    manufacturer = models.CharField(max_length=80)
    cost_in_credits = models.CharField(max_length=40)
    length = models.CharField(max_length=40)
    max_atmosphering_speed = models.CharField(max_length=40)
    crew = models.CharField(max_length=40)
    passengers = models.CharField(max_length=40)
    cargo_capacity = models.CharField(max_length=40)
    consumables = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name


class Starship(Transport):
    """ A starship is a transport with a hypderdrive """

    hyperdrive_rating = models.CharField(max_length=40)
    MGLT = models.CharField(max_length=40)
    starship_class = models.CharField(max_length=40)
    pilots = models.ManyToManyField(People, related_name="starships", blank=True)


class Vehicle(Transport):
    """ A vehicle is anything without hyperdrive capability """

    vehicle_class = models.CharField(max_length=40)
    pilots = models.ManyToManyField(People, related_name="vehicles", blank=True)
