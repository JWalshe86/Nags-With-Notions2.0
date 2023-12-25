from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Booking(models.Model):
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    event_date = models.DateTimeField(null=True)
    location = models.CharField(("address"), max_length=128, blank=True)
    guest_nos = models.IntegerField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    