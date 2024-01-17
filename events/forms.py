from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'slug', 'author', 'content', 'event_image', 'status')
                
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter event title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.NumberInput(attrs={'class': 'form-control'}),
        }