
from django import forms
from .models import Booking


# Create a booking form
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'location', 'phone', 'booking_date','guest_number', 'message','status')
        
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control, w-50,'}),
            'location': forms.Textarea(attrs={'class': 'form-control, input-sm', 'rows': '3', 'placeholder': 'Please enter venue location'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'guest_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter  any additional info.'}),
            'status': forms.Select(attrs={'class': 'form-control, w-20'}),
        }
        