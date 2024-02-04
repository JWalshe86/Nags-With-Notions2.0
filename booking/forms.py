from django import forms


# Create a booking form
class BookingForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)
        

