from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.views import generic
from .models import Event
from .forms import EventForm

# Create your views here.
class EventList(generic.ListView):
    queryset = Event.objects.all()
    template_name = "events/index.html"
    paginate_by = 3

@permission_required("events.view_event")
def createEvent(request):
    
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/events')
            
    context={'form': form}
    return render(request, 'events/event_form.html', context)

@permission_required("events.view_event")
def updateEvent(request, pk):
    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('/events')
    context = {'form': form}
    return render(request, 'events/event_form.html', context)
    
    
@permission_required("events.view_event")
def deleteEvent(request, pk):
    event = Event.objects.get(id=pk)
    if request.method == "POST":
        event.delete()
        return redirect('/events')
    context = {'event': event}
    return render(request, 'events/delete.html', context)
    
    
    