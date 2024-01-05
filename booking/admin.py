from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ('name', 'status', 'created_on')
    search_fields = ['name', 'message']
    list_filter = ('status', 'created_on')
    summernote_fields = ('message',)


