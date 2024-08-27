from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pizza_system import views as user_views

urlpatterns = [
    path('', include('pizza_system.urls')),
    path('summernote/', include('django_summernote.urls')),
    path("accounts/", include("allauth.urls")),
    path("events/", include("events.urls"), name="events-urls"),
    path('', include('booking.urls')),
    path('admin/', admin.site.urls),
]

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'nags_with_notions.views.handling_404'

