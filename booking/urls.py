from . import views
from django.urls import path

urlpatterns = [
    path('bookings/', views.BookingList.as_view()),
]