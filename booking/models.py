from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Booked"))

class Book(models.Model):
    name = models.ForeignKey(
        User, on_delete=models.CASCADE,
    )
    phone = PhoneNumberField()
    