import factory
from booking.models import Booking

class BookingFactory(factory.Factory):
    class Meta:
        model = Booking

def test_factory_fixture(booking_factory):
    location = booking_factory(name="Ratoath")
    assert location.name == "Ratoath"