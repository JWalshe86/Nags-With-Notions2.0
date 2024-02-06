from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE, null=True, related_name='booking')
    name = models.CharField(max_length=200)
    booking_date = models.CharField(max_length=200)
    location = models.CharField(max_length=150)
    guest_number = models.IntegerField(default=10)
    message = models.CharField()
    created_on = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.name
    

    

    
    
    
    
    
    
    
    
