from django.test import SimpleTestCase
from django.urls import reverse, resolve
from booking.views import CustomLoginView, RegisterPage, BookingList, BookingCreate, BookingUpdate, BookingDelete

class TestUrls(SimpleTestCase):
    
    def test_create_booking_url_is_resolved(self):
        url = reverse('create_booking')
        self.assertEqual(resolve(url).func.view_class, BookingCreate)
        
    def test_booking_update_url_is_resolved(self):
        url = reverse('update_booking', args=[1988])
        self.assertEqual(resolve(url).func.view_class, BookingUpdate)