from pytest_factoryboy import register

from .factories import EventFactory

register(EventFactory)  # => author_factory
