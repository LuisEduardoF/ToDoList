from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name","day", "hour","dur","description","color"]

        widget = {'name': forms.TextInput(attrs={'class':'form-control'}), 
        'day': forms.DateTimeInput(attrs={'class':'form-control'}), 
        'hour': forms.Select(attrs={'class':'form-control'}), 
        'dur': forms.TextInput(attrs={'class':'form-control'}), 
        'description': forms.Textarea(attrs={'class':'form-control'}), 
        'color': forms.TextInput(attrs={'class':'form-control'})}
