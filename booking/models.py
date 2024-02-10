from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True, blank=True, related_name='booking')
    booking_date = models.CharField(max_length=200)
    location = models.CharField(max_length=150)
    guest_number = models.IntegerField(default=10)
    message = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.message
    
    class Meta:
        ordering = ['-created_on']
    

    

    
    
    
    
    
    
    
    
