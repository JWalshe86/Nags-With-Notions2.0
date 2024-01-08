from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import BookingForm

# Create your views here.

def booking(request):
    """
    Renders the booking page
    """
    submitted = False
    if request.method == "POST":
        booking_form = BookingForm(request.POST)
        print('booking form valid', booking_form.is_valid(), booking_form.errors)
        if booking_form.is_valid():
            booking_form.save()
            return HttpResponseRedirect('/bookings?submitted=True')
    else:
        booking_form = BookingForm()
        if 'submitted' in request.GET:
            submitted = True

    booking_form = BookingForm()

    return render(
        request,
        "bookings.html",
        {
            "booking_form": booking_form,
            "submitted": submitted
        },
    )