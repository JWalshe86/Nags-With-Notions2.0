from django.shortcuts import render, redirect
from django.views import generic
from .models import Event
from .forms import EventForm

# Create your views here.
class EventList(generic.ListView):
    queryset = Event.objects.all()
    template_name = "events/index.html"
    paginate_by = 3


def createEvent(request):
    
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            
    context={'form': form}
    return render(request, 'events/event_form.html', context)

def updateEvent(request, pk):
    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'events/event_form.html', context)
    
def deleteEvent(request, pk):
    event = Event.objects.get(id=pk)
    if request.method == "POST":
        event.delete()
        return redirect('/')
    context = {'event': event}
    return render(request, 'events/delete.html', context)
    
    
    