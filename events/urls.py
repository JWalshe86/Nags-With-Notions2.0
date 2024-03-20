"imports"
from django.urls import path
from .views import EventList, CreateEvent, UpdateEvent, DeleteEvent


urlpatterns = [
    path('', EventList.as_view(), name='events'),
    path('events/', CreateEvent.as_view(), name="create_event"),
    path('update_event/<str:pk>', UpdateEvent.as_view(), name="update_event"),
    path('delete_event/<str:pk>', DeleteEvent.as_view(), name="delete_event"),
]
