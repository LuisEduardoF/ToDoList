from django.db import models
from django import template
import random
from datetime import date

# Event -> Routine (Day-by-Day events)
#       -> Schedule (Scheduled Events)

# Create your views here.
class Event(models.Model):
    hour = models.DateTimeField(verbose_name="")
    day = models.DateTimeField(verbose_name="")
    dur = models.DurationField(verbose_name="")
    name = models.CharField(max_length=10, verbose_name="")
    description = models.CharField(max_length=200, verbose_name="")
    color = models.CharField(max_length=200, default="", verbose_name="")


class Routine(Event):
    repeat = models.JSONField(default=dict)
    
    @classmethod
    def create(cls, name, day, hour, description, repeat):
        rtn = cls(name = name, day=day, hour=hour, description=description, repeat=repeat)
        return rtn

class Schedule(Event):

    @classmethod
    def create(cls, name, day, hour):
        sch = cls(name = name, day=day, hour=hour, description=description)
        return sch
    
class Day(models.Model):
    datetime = models.TimeField()
    color = models.CharField(max_length=200)