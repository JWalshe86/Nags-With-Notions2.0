"imports"
from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    "creates detail for events form"

    class Meta:
        "creates form using event model template"
        model = Event
        fields = ["start_date", "description", "image"]
