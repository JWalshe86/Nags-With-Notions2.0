from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
class Item(models.Model):
    
    booking = models.ForeignKey(Booking, default=1, on_delete=models.CASCADE)
    location = models.CharField(max_length=150)
    phone = PhoneNumberField()
    booking_date = models.DateField()
    guest_number = models.IntegerField(default='')
    message = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f"Booking request from {self.location}"
    
    
    
    
    
    
    
    
