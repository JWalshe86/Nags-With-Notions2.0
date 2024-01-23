import factory
from events.models import Event

class EventFactory(factory.Factory):
    class Meta:
        model = Event


def test_factory_fixture(event_factory):
    title = event_factory(name="Charles Dickens")
    assert title.name == "Charles Dickens"