from django.shortcuts import render


def handling_404(request, exception):
    render(request,'404.html')
    
    