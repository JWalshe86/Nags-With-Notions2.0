from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from booking.views import CustomLoginView, RegisterPage

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', views.myview, name='home'),
]