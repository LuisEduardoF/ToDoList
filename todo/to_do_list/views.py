from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to my app!")

def event_list(request):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    events = [Routine(hour=2, day=10, dur=3, name="Medico", description="Medico do ombro", repeat={d:False for d in days})]
    print(events[0].repeat)
    
    return render(request, 'main/main.html', {'days': days,'events': events})