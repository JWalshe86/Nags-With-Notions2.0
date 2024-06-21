"imports"
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Booking

class CustomLoginView(LoginView):
    "This module renders a template whereby a user can login to the website"
    template_name = 'booking/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

class RegisterPage(SuccessMessageMixin, FormView):
    "This module renders a registeration form whereby a user can register to the site"
    template_name = 'booking/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_message = 'New Account Created'
    success_url = reverse_lazy('home')

   # automatically login user
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        "function enables user to get own bookings"
        if self.request.user.is_authenticated:
            return redirect('view')
        return super(RegisterPage, self).get(*args, **kwargs)

class BookingList(LoginRequiredMixin, ListView):
    """
    Renders the booking page
    """
    model = Booking
    context_object_name = 'bookings'
    template_name = 'booking/bookings.html'

    # users can only see own data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookings'] = context['bookings'].filter(user=self.request.user)
        return context

class BookingCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    "This module renders a form whereby users can book Nags with Notions services"

    model = Booking
    fields = ['booking_date', 'location', 'guest_number', 'message']
    success_message = 'New booking created'
    success_url = reverse_lazy('view')

    # over-ride is valid method
    def form_valid(self, form):
        # user can't create bookings for other users
        form.instance.user = self.request.user
        return super(BookingCreate, self).form_valid(form)

class BookingUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    "This module allows users to update their bookings"

    model = Booking
    fields = ['booking_date', 'location', 'guest_number', 'message']
    success_message = 'Booking updated'
    success_url = reverse_lazy('view')

class BookingDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    "This module allows users delete their bookings"

    model = Booking
    context_object_name = 'booking'
    success_message = 'Booking deleted'
    success_url = reverse_lazy('view')

def view(request):
    "This module allows user see their bookings"
    return render(request, "view.html", {} )
