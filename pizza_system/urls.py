from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from booking.views import CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.myview, name='home'),
    path('index/', views.index, name='index')
]