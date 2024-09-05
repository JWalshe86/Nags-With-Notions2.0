from django.db import models  # Ensure this import is present

class Event(models.Model):
    "creates event model"
    name = models.CharField(max_length=200)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)  # Added upload_to
    description = models.TextField(max_length=1024, null=True, blank=True)
    start_date = models.DateTimeField()

    def __str__(self):
        "returns name"
        return f"{self.name}"

