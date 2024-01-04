from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Booked"))

class Booking(models.Model):
    name = models.ForeignKey(
        User, on_delete=models.CASCADE,
    )
    phone = PhoneNumberField()
    booking_date = models.DateTimeField()
    guest_number = models.IntegerField()
    message = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    