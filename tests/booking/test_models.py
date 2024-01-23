import factory
from pytest_factoryboy import register
from tests.factories import Booking

@register
class AuthorFactory(factory.Factory):
    class Meta:
        model = Booking

    location = "Ratoath"


def test_model_fixture(booking):
    assert booking.location == "Ratoath"
