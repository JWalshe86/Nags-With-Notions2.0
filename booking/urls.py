"imports"
from django.urls import path
from .views import BookingList, BookingCreate, BookingUpdate, BookingDelete

urlpatterns = [
    path('create_booking/', BookingCreate.as_view(), name="create_booking"),
    path('update_booking/<int:pk>', BookingUpdate.as_view(), name="update_booking"),
    path('delete_booking/<int:pk>/', BookingDelete.as_view(), name="delete_booking"),
    path('view/', BookingList.as_view(), name='view'),
]
