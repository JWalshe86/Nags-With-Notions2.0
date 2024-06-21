"imports"
from django.urls import path
from . import views


urlpatterns = [
    path("events", views.Event, name="events"),
    path("add_event", views.add_event, name="add_event"),
    path("edit/<int:event_id>/", views.edit_event, name="edit_event"),
    path("<int:event_id>/", views.event_detail, name="event_detail"),
    path("delete/<int:event_id>/", views.delete_event, name="delete_event"),
]
