from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


