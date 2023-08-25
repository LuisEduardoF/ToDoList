from django import forms
from .models import Event
import datetime as dt
COLOR_CHOICES = [(c, c.capitalize()) for c in ["yellow", "green", "brown", "blue", "purple", "orange"]]
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name","day", "hour","description","color"]

        widgets = {
        "name": forms.TextInput(attrs={"class": "form-control custom-input", "placeholder": "Name"}),
        "day": forms.DateInput(attrs={"class": "form-control custom-input", "placeholder": "Date", "onfocus":"(this.type='date')"}),
        "hour": forms.TextInput(attrs={"class": "form-control custom-input", "placeholder": "Hour", "onfocus":"(this.type='time')", "min": "07:00", "max":"22:00"}),
        "description": forms.Textarea(attrs={"class": "form-control custom-input", "placeholder": "Description"}),
        "color": forms.Select(choices=COLOR_CHOICES, attrs={"class": "form-control custom-input colors", "placeholder": "Color", "id":"colors", "onfocus":"(this.type='color')", "onchange":"change();"}),
    }
