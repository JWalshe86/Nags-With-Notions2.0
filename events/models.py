"imports"
from django.db import models


class Event(models.Model):
    "creates event model"
    name = models.CharField(max_length=200, unique=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(max_length=1024, null=True, blank=True)
    start_date = models.DateTimeField()


    def __str__(self):
        "returns name"
        return f"{self.name}"
