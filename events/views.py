from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import Event
from .forms import EventForm

# Create your views here.
class EventList(ListView):
   
    model = Event
    # context_object_name = 'events'
    template_name = "events/index.html"
    paginate_by = 3

# @permission_required("events.view_event")
class createEvent(SuccessMessageMixin, CreateView):
    
    model = Event
    fields = ['title', 'content', 'event_image']
    success_message = 'New Event Created'
    success_url = reverse_lazy('events')
    
    # over-ride is valid method
    def form_valid(self, form):
        # user can't create bookings for other users
        form.instance.user = self.request.user
        return super(createEvent, self).form_valid(form)

# @permission_required("events.view_event")
class updateEvent(SuccessMessageMixin, UpdateView):
    
    model = Event
    fields = ['title', 'content', 'event_image']
    success_message = 'Event updated'
    success_url = reverse_lazy('events')
    
    
# @permission_required("events.view_event")

class deleteEvent(SuccessMessageMixin, DeleteView):
    
    model = Event
    context_object_name = 'events'
    success_message = 'Event deleted'
    success_url = reverse_lazy('events')
    
    
    
    