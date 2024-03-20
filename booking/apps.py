"imports"
from django.apps import AppConfig


class BookingConfig(AppConfig):
    "add booking config to database admin"
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'
