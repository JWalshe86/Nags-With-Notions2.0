from django.urls import path
from django.views.generic import TemplateView
from .views import contact_view, index_view
from django.contrib.auth.views import LogoutView
from . import views
from booking.views import CustomLoginView, RegisterPage

urlpatterns = [
    path('', index_view, name='index'),  # Ensure this is the view rendering index.html
    path('contact/', contact_view, name='contact'),
    path('contact_success/', TemplateView.as_view(template_name='contact_success.html'), name='contact_success'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', views.index_view, name='home'),
]


