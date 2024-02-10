from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import BookingForm
from .models import Booking

class CustomLoginView(LoginView):
    template_name = 'booking/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self): 
        return reverse_lazy('view')

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
    
class BookingDetail(LoginRequiredMixin, DetailView):

    model = Booking
    context_object_name = 'booking'
    template_name = 'booking/booking.html'   
    
class BookingCreate(LoginRequiredMixin, CreateView):
    
    model = Booking
    fields = ['booking_date', 'location', 'guest_number', 'message']
    success_url = reverse_lazy('view')
    
    # over-ride is valid method
    def form_valid(self, form):
        # user can't create bookings for other users
        form.instance.user = self.request.user
        return super(BookingCreate, self).form_valid(form)
    
class BookingUpdate(LoginRequiredMixin, UpdateView):
    
    model = Booking
    fields = ['booking_date', 'location', 'guest_number', 'message']
    success_url = reverse_lazy('view')
    
class BookingDelete(LoginRequiredMixin, DeleteView):
    
    model = Booking
    context_object_name = 'booking'
    success_url = reverse_lazy('view') 
    
def view(request):
    return render(request, "view.html", {} )
    
    
    
    