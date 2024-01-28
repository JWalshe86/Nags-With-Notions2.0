from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
STATUS = (('draft', "Draft"), ('booked', "Booked"))

class Booking(models.Model):
    name = models.CharField(
max_length=150    )
    location = models.CharField(max_length=150)
    phone = PhoneNumberField()
    booking_date = models.DateField()
    guest_number = models.IntegerField(default='')
    message = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default="draft")
    
    def __str__(self):
        return f"Booking request from {self.name}"