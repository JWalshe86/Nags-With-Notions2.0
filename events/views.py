"imports"
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Event

# Create your views here.
class EventList(ListView):
    "renders a page where a user can view events"

    model = Event
    # context_object_name = 'events'
    template_name = "events/index.html"
    paginate_by = 3

# @permission_required("events.view_event")
class CreateEvent(SuccessMessageMixin, CreateView):
    "renders form so superusers can create an event"

    model = Event
    fields = ['title', 'content', 'event_image']
    success_message = 'New Event Created'
    success_url = reverse_lazy('events')

    # over-ride is valid method
    def form_valid(self, form):
        # user can't create bookings for other users
        form.instance.user = self.request.user
        return super(CreateEvent, self).form_valid(form)

# @permission_required("events.view_event")
class UpdateEvent(SuccessMessageMixin, UpdateView):
    "renders form so superusers can update events"

    model = Event
    fields = ['title', 'content', 'event_image']
    success_message = 'Event updated'
    success_url = reverse_lazy('events')


# @permission_required("events.view_event")

class DeleteEvent(SuccessMessageMixin, DeleteView):
    "renders form so users can delete events"

    model = Event
    context_object_name = 'events'
    success_message = 'Event deleted'
    success_url = reverse_lazy('events')
