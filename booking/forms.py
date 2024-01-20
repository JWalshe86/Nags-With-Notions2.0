
from django import forms
from .models import Booking


# Create a booking form
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'location', 'phone', 'booking_date','guest_number', 'message','status')
        
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter venue location'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter contact number'}),
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Please enter date of event'}),
            'guest_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter estimated guest number'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter  any additional info.'}),
            'status': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        