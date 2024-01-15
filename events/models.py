from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="events"   
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    event_image = models.ImageField(null=True, blank=True, upload_to="images/")
    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"{self.title}"
    
    
class Comment(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["created_on"]
    