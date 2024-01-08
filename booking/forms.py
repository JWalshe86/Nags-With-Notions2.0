from django import forms
from .models import Booking


# Create a booking form
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ("name", "phone", "booking_date", "guest_number", "message", "status")
        labels = {
            'name': '',
            'phone': '',
            'booking_date': '',
            'guest_number': '',
            'message': '',
            'status': '',
        }
        
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'booking_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter booking date'}),
            'guest_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter guest numbers'}),
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Message'}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        }