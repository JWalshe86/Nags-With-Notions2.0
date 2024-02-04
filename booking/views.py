from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import BookingForm
from .models import Booking, Item

# Create your views here.

def booking(request, id):
    """
    Renders the booking page
    """
    ls = Booking.objects.get(id=id)
    item = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(item.location)))
    # booking_form = BookingForm()
    # bookings_list = Booking.objects.all()
    
    
    
@login_required(login_url='login')
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
    
    
    
    
    
    