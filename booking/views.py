from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .forms import BookingForm
from .models import Booking

# Create your views here.

def booking(request, id):
    """
    Renders the booking page
    """
    booking = Booking.objects.get(id=id)
    
    
    return render(request,"bookings.html", {'booking': booking})
    # booking_form = BookingForm()
    # bookings_list = Booking.objects.all()
    
    
    
@login_required(login_url='login')
def createBooking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = Booking(name=n)
            t.save()
            return HttpResponseRedirect('bookings/%i' %t.id)
    else:
        form = BookingForm()
    
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
    
    
    
    
    
    