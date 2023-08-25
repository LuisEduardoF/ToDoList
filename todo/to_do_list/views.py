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

class EventCreateView(FormView):
    model = Event
    form_class = EventForm
    template_name = 'forms/event_form.html'  # Create this template
    success_url = '/main'  # Redirect to a success page

def event_list(request):
    days = ["Today"]
    events = [Routine(hour=2, day=date.today(), dur=3, name="Medico", description="Medico do ombro", color=getRandRGB(), repeat={"Monday":True, "Tuesday":False, "Wednesday":False, "Thursday":False, "Friday":False, "Saturday":False, "Sunday":False})]
    return render(request, 'main/main.html', {'days': days,'events': events, 'color':getRandRGB(), 'form':EventForm()})
