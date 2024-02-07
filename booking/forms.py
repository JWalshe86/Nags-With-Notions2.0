from django import forms
from booking.models import Booking


# Create a booking form
class BookingForm(forms.ModelForm):
    location = forms.CharField(label="location", max_length=200)
    booking_date = forms.CharField()
    guest_number = forms.IntegerField()
    message = forms.CharField(label="message", max_length=200)

    class Meta:
        model = Booking
        fields = '__all__'
