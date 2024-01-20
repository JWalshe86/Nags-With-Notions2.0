from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking

# Create your views here.

def booking(request):
    """
    Renders the booking page
    """
    booking_form = BookingForm()
    bookings_list = Booking.objects.all()

    return render(
        request,
        "bookings.html",
        {
            "booking_form": booking_form,
            "bookings_list": bookings_list,
        },
    )
    
def createBooking(request):
    
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            
    
    context = {'form': form}
    return render(request, 'booking_form.html', context)

def updateBooking(request, pk):
    
    booking = Booking.objects.get(id=pk)
    form = BookingForm(instance=booking)
    
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('/bookings/')
    
    context = {'form': form}
    return render(request, 'booking_form.html', context)

def deleteBooking(request, pk):
    booking = Booking.objects.get(id=pk)
    print('in deletebooking', booking, request)
    if request.method == "POST":
        print('POSTED')
        booking.delete()
        return redirect('/bookings/')
        
    context = {'booking': booking}
    return render(request, 'delete.html', context)
    
    
    
    
    
    