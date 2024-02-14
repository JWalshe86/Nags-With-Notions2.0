from django.db import models

STATUS = ((0, "Draft"), (1, "Published"))

from django.db import models

# Create your models here.

class Event(models.Model):
    author =  models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    event_image = models.ImageField(null=True, blank=True, upload_to="images/")
    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"{self.title}"
    

    
    