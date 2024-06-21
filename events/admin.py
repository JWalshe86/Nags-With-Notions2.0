"imports"
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Event

@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    "Adds Summernote functionality to db admin"
    list_display = ('title', 'content', 'event_image')
    search_fields = ['title']
    summernote_fields = 'content'
