from django.db import models
from django import template
import random
from datetime import date

# Event -> Routine (Day-by-Day events)
#       -> Schedule (Scheduled Events)

# Create your views here.
class Event(models.Model):
    hour = models.DateTimeField()
    day = models.DateTimeField()
    dur = models.DurationField()
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=200)
    color = models.CharField(max_length=200, default="blue")


class Routine(Event):
    repeat = models.JSONField(default=dict)
    
    @classmethod
    def create(cls, name, day, hour, dur, description, repeat):
        rtn = cls(name = name, day=day, dur=dur, hour=hour, description=description, repeat=repeat)
        return rtn

class Schedule(Event):

    @classmethod
    def create(cls, name, day, hour, dur):
        sch = cls(name = name, day=day, dur=dur, hour=hour, description=description)
        return sch
    
class Day(models.Model):
    datetime = models.TimeField()
    color = models.CharField(max_length=200)