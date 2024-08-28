from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(label='Email address', max_length=255)
    message = forms.CharField(label='Message', widget=forms.Textarea)



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name' : 'Name', 
            'email' : 'Email',
        }
