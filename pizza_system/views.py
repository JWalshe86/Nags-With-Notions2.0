from django.shortcuts import render

# Create your views here.
def myview(request):
    print('request:', request)
    return render(request, "index.html")