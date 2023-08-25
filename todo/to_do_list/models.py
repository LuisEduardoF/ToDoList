from django.db import models
from django import template
import random
from datetime import date

# Event -> Routine (Day-by-Day events)
#       -> Schedule (Scheduled Events)

# Create your views here.
class Event(models.Model):
    date = models.DateTimeField(verbose_name="", default="2000-11-29T11:11", unique=True)
    name = models.CharField(max_length=50, verbose_name="")
    description = models.CharField(max_length=200, verbose_name="")
    color = models.CharField(max_length=200, default="Yellow", verbose_name="")
    id_user = models.IntegerField(primary_key=True)
    # Testing
    @classmethod
    def create(cls, id_user, name, date, description, repeat):
        event = cls(id_user=id_user, name=name, date=date, description=description)
        return event
    
class Day(models.Model):
    datetime = models.DateField(primary_key = True, default="2000-11-29")
    color = models.CharField(max_length=200)
    
    @classmethod
    def create(cls, datetime, color):
        day = cls(datetime=datetime, color=color)
        return day