from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    email = models.EmailField(max_length=254)
    phone = models.PhoneNumberField()
    event_date = 
    location =
    guest_nos =
    message =
    create_on = 
    