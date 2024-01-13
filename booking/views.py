from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import BookingForm
from .models import Booking

# Create your views here.

def booking(request):
    """
    Renders the booking page
    """
    booking_form = BookingForm()
    bookings_list = Booking.objects.all()
    submitted = False
    if request.method == "POST":
        booking_form = BookingForm(request.POST)
        print('booking form valid', booking_form.is_valid(), booking_form.errors)
        if 'delete' in request.POST:
            pk = request.POST.get('delete')
            booking = Booking.objects.get(id=pk)
            booking.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            booking = Booking.objects.get(id=pk)
            booking_form = BookingForm(instance=booking)
            print('editeor',booking_form)
        elif booking_form.is_valid():
            booking_form.save()
            return HttpResponseRedirect('/bookings?submitted=True')
    else:
        booking_form = BookingForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(
        request,
        "bookings.html",
        {
            "booking_form": booking_form,
            "bookings_list": bookings_list,
            "submitted": submitted
        },
    )
    
