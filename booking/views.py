from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .forms import BookingForm
from .models import Booking

# Create your views here.

def booking(request):
    """
    Renders the booking page
    """
    booking = Booking.objects.all()
            
    # user specific bookings
    if booking in request.user.booking.all():
        return render(request,"view.html", {'booking': booking})
    
    return render(request,"view.html", {})
    
    
@login_required(login_url='login')
def createBooking(request):
    if request.method == 'POST':
        formset = BookingForm(request.POST)
        
        if formset.is_valid():
            print('in here', formset)
            formset.save()
            
            return redirect('/view')
    else:
        formset = BookingForm()
        return render(request, 'booking_form.html', {'formset': formset})

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
    
    
def view(request):
    return render(request, "view.html", {} )
    
    
    
    