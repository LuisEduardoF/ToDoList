from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from .models import *
from .forms import EventForm
import random
from datetime import date
# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to my app!")

def getRandRGB():
    return random.choice(["green", "yellow", "brown", "blue", "purple", "orange"])

def event_list(request):
    days = ["Friday"]
    events = [Routine(hour=2, day=date.today().strftime("%A"), name="Medico", description="Medico do ombro", color=getRandRGB(), repeat={"Monday":True, "Tuesday":False, "Wednesday":False, "Thursday":False, "Friday":True, "Saturday":False, "Sunday":False})]

    return render(request, 'main/main.html', {'days': days,'events': events, 'color':getRandRGB(), 'form':EventForm()})
