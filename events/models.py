"imports"
from django.db import models

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Event(models.Model):
    "creates event model"
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    event_image = models.ImageField(null=True, blank=True, upload_to="images/")

    class Meta:
        "events order from top to bottom"
        ordering = ["-created_on"]

    def __str__(self):
        "returns title"
        return f"{self.title}"
