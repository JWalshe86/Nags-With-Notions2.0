from . import views
from django.urls import path

urlpatterns = [
    path('bookings/', views.booking, name='bookings'),
    path('bookings-list/', views.all_bookings, name='bookings-list'),
]