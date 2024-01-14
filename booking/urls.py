from . import views
from django.urls import path

urlpatterns = [
    path('bookings/', views.booking, name='bookings'),
    path('create_booking/', views.createBooking, name="create_booking"),
    path('update_booking/<str:pk>/', views.updateBooking, name="update_booking"),
    path('delete_booking/<str:pk>/', views.deleteBooking, name="delete_booking"),
]