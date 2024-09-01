from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import send_mail
from django.conf import settings
from .forms import CustomUserCreationForm, PizzaForm, ContactForm
from .models import Pizza

# Decorator to check if user is a superuser
def superuser_required(function):
    return user_passes_test(lambda u: u.is_superuser)(function)

# Index view
def index_view(request):
    pizzas = Pizza.objects.all()  # Query all pizza objects
    return render(request, 'index.html', {'pizzas': pizzas})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # List of recipient emails
            recipient_list = [settings.EMAIL_HOST_USER, 'hello@nagswithnotions.com', 'walshejohnnyw7@gmail.com']
            
            try:
                send_mail(
                    subject='Contact Form Message',
                    message=f"Message from {email}:\n\n{message}",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=recipient_list,
                )
                messages.success(request, 'Thank you for your message. We will get back to you shortly.')
                return redirect('contact_success')
            except Exception as e:
                messages.error(request, 'There was an error sending your message. Please try again later.')
                return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


# Edit Pizza view
@superuser_required
def edit_pizza(request, pk):
    pizza = get_object_or_404(Pizza, pk=pk)
    if request.method == 'POST':
        form = PizzaForm(request.POST, request.FILES, instance=pizza)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pizza updated successfully!')
            return redirect('pizza_list')  # Redirect to the list or another page
    else:
        form = PizzaForm(instance=pizza)
    return render(request, 'edit_pizza.html', {'form': form})

# Delete Pizza view
@superuser_required
def delete_pizza(request, pk):
    pizza = get_object_or_404(Pizza, pk=pk)
    if request.method == 'POST':
        pizza.delete()
        messages.success(request, 'Pizza deleted successfully!')
        return redirect('pizza_list')  # Redirect to the list or another page
    return render(request, 'confirm_delete.html', {'pizza': pizza})



