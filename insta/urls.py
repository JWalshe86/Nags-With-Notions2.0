from django.urls import path
from .views import instagram_home

urlpatterns = [
    path('', instagram_home, name='instagram_home'),
]

