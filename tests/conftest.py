from pytest_factoryboy import register

from .factories import BookingFactory

register(BookingFactory)  # => author_factory
