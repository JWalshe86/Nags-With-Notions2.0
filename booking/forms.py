from django.forms import ModelForm
from .models import Booking


# Create a booking form
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        