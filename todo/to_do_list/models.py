from django.db import models
from django import template
# Event -> Routine (Day-by-Day events)
#       -> Schedule (Scheduled Events)

# Create your views here.
class Event(models.Model):
    hour = models.TimeField()
    day = models.TimeField()
    dur = models.IntegerField()
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=200)


class Routine(Event):
    repeat = models.JSONField()
    
    @classmethod
    def create(cls, name, day, hour, dur, description, repeat):
        rtn = cls(name = name, day=day, dur=dur, hour=hour, description=description, repeat=repeat)
        return rtn

class Schedule(Event):

    @classmethod
    def create(cls, name, day, hour, dur):
        sch = cls(name = name, day=day, dur=dur, hour=hour, description=description)
        return sch