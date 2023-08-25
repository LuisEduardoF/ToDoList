from django import forms
from .models import Event
import datetime as dt
COLOR_CHOICES = [(c, c.capitalize()) for c in ["yellow", "green", "brown", "blue", "purple", "orange"]]
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "date", "description","color"]

        widgets = {
        "name": forms.TextInput(attrs={"class": "form-control custom-input", "placeholder": "Name"}),
        "date": forms.DateTimeInput(attrs={"type":"datetime-local", "class": "form-control custom-input", "placeholder": "Date", "min":str(dt.date.today())}),
        "description": forms.Textarea(attrs={"class": "form-control custom-input", "placeholder": "Description"}),
        "color": forms.Select(choices=COLOR_CHOICES, attrs={"class": "form-control custom-input colors", "placeholder": "Color", "id":"colors", "onfocus":"(this.type='color')", "onchange":"change();"}),
        }

        required = {
            "name": True,      # Mark the "name" field as required
            "date": True,
            "description": False,  # Mark the "description" field as required
            "color": True,     # Mark the "color" field as required
        }
