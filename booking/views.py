from django.shortcuts import render
from django.views import generic
from .models import Booking

# Create your views here.

class BookingList(generic.ListView):
    model = Booking