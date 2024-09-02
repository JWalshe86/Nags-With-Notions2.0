from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .models import Event
from .forms import EventForm


def all_events(request):
    """A view to show all events, including sorting and search queries"""

    events = Event.objects.all()

    context = {
        "events": events,
    }
    return render(request, "events/index.html", context)


def event_detail(request, event_id):
    """A view to show event details"""

    event = get_object_or_404(Event, pk=event_id)

    context = {
        "event": event,
    }
    return render(request, "events/event_detail.html", context)


@login_required
def add_event(request):
    """Add a event to the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("index"))

    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            messages.success(request, "Successfully added event!")
            return redirect(reverse("event_detail", args=[event.id]))
        else:
            messages.error(
                request,
                "Failed to add event. Please ensure the form is valid.",
            )
    else:
        form = EventForm()

    template = "events/add_event.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_event(request, event_id):
    """Edit a event in the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("index"))
    event = get_object_or_404(Event, pk=event_id)
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated event!")
            return redirect(reverse("all_events"))
        else:
            messages.error(
                request,
                "Failed to update event. Please ensure the form is valid.",
            )
    else:
        form = EventForm(instance=event)
        messages.info(request, f"You are editing {event.name}")

    template = "events/edit_event.html"
    context = {
        "form": form,
        "event": event,
    }

    return render(request, template, context)


@login_required
def delete_event(request, event_id):
    """Delete a event from the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("index"))
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    messages.success(request, "Event deleted!")
    return redirect(reverse("all_events"))
