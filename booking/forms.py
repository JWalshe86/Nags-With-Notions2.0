from django import forms
from .models import Booking


# Create a booking form
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name']
        

