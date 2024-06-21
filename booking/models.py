"imports"
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    "creates booking model"
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1,
    null=True, blank=True, related_name='booking')
    booking_date = models.CharField(max_length=200)
    location = models.CharField(max_length=150)
    guest_number = models.IntegerField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        "returns message as a string"
        return self.message

    class Meta:
        "puts order from top to bottom"
        ordering = ['-created_on']
