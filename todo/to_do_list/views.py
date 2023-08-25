from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import EventForm
import random
from datetime import date, datetime
# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to my app!")

def getRandRGB():
    return random.choice(["green", "yellow", "brown", "blue", "purple", "orange"])

def event_list(request):
    events = [{"id": e["id_user"], "date":e["date"].date(), "name":e["name"], "day":e["date"].strftime("%d/%m/%Y"), "hour":e["date"].strftime("%H:%m"), "description":e["description"], "color":e["color"]} for e in Event.objects.all().values()]
    days = [{"name":d["datetime"].strftime("%A"),"datetime": d["datetime"],"color": d["color"]} for d in Day.objects.all().values()]
    
    events.sort(key=lambda x: x["hour"])
    days.sort(key=lambda x: x["datetime"])
    
    return render(request, 'main/main.html', {'days': days,'events': events, 'form':EventForm()})

@csrf_exempt
def receive_data(request):
    if request.method == 'POST':
        res = request.POST.dict()
        d = datetime.strptime(res["date"], "%Y-%m-%dT%H:%M").date()
        print("D", d)
        if(not Day.objects.filter(datetime=d).exists()):
            Day.objects.create(datetime=d, color=getRandRGB())
        print("Entrou em Receive")
        new_id = len(Event.objects.all().values())
        Event.objects.create(id_user=new_id+1, date=res["date"], name=res["name"], description=res["description"], color=res["color"])
        return JsonResponse({'message': 'Data received successfully'})
    else:
        return JsonResponse({'message': 'Data not received successfully'})

@csrf_exempt
def change_data(request):
    if request.method == 'POST':
        res = request.POST.dict()
        print(res)
        id = res["id"]
        print("Entrou em Change")
        Event.objects.filter(id=id).delete()
        return JsonResponse({'message': 'Data received successfully'})
    else:
        return JsonResponse({'message': 'Data not received successfully'})