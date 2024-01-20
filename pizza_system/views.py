from django.shortcuts import render
from django.views import generic

# Create your views here.
def myview(request):
    print('request:', request)
    return render(request, "index.html")