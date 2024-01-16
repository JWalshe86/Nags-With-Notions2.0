from django.urls import path
from . import views


urlpatterns = [
    path('', views.EventList.as_view(), name='events'),
    path('events/', views.createEvent, name="create_event"),
    path('update_event/<str:pk>', views.updateEvent, name="update_event"),
    path('delete_event/<str:pk>', views.deleteEvent, name="delete_event"),
]