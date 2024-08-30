from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import CustomUserCreationForm
from booking.views import CustomLoginView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

# views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse



# Create your views here.
def index_view(request):
    return render(request, 'index.html')


def contact_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # List of recipient emails
        recipient_list = [settings.EMAIL_HOST_USER, 'hello@nagswithnotions.com', 'walshejohnnyw7@gmail.com']  # Add additional emails here
        
        try:
            # Send the email
            send_mail(
                subject='Contact Form Message',
                message=f"Message from {email}:\n\n{message}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=recipient_list,
            )
            return HttpResponse('Thank you for your message. We will get back to you shortly.')
        except Exception as e:
            # Log or handle the exception
            return HttpResponse('There was an error sending your message. Please try again later.')
    
    return render(request, 'index.html')

