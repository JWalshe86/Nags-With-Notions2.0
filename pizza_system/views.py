from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import CustomUserCreationForm
from booking.views import CustomLoginView

# Create your views here.
def myview(request):
    return render(request, "index.html", {})





