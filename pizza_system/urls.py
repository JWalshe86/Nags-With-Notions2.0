from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from .views import contact_view, index_view, edit_pizza, delete_pizza, pizza_list
from booking.views import CustomLoginView, RegisterPage

urlpatterns = [
    path('', index_view, name='index'),  # Ensure this is the view rendering index.html
    path('contact/', contact_view, name='contact'),
    path('contact_success/', TemplateView.as_view(template_name='contact_success.html'), name='contact_success'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('pizza-list/', pizza_list, name='pizza_list'),  # Add this URL pattern
    path('edit_pizza/<int:pk>/', edit_pizza, name='edit_pizza'),
    path('delete_pizza/<int:pk>/', delete_pizza, name='delete_pizza'),
]

