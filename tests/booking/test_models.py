import factory
from pytest_factoryboy import register
from tests.factories import Event

@register
class AuthorFactory(factory.Factory):
    class Meta:
        model = Event

    title = "Charles Dickens"


def test_model_fixture(event):
    assert event.title == "Charles Dickens"