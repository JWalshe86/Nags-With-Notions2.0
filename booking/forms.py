"imports"
from django import forms
from booking.models import Booking


# Create a booking form
class BookingForm(forms.ModelForm):
    "adds form detail for booking form"
    location = forms.CharField(label="location", max_length=200)
    booking_date = forms.CharField()
    guest_number = forms.IntegerField()
    message = forms.CharField(label="message", max_length=200)

    class Meta:
        "renders all fields from model into booking form"
        model = Booking
        fields = '__all__'
