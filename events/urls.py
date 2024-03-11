from django.urls import path
from .views import EventList, createEvent, updateEvent, deleteEvent


urlpatterns = [
    path('', EventList.as_view(), name='events'),
    path('events/', createEvent.as_view(), name="create_event"),
    path('update_event/<str:pk>', updateEvent.as_view(), name="update_event"),
    path('delete_event/<str:pk>', deleteEvent.as_view(), name="delete_event"),
]
