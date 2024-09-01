from django.contrib import admin
from .models import Todolist, Pizza


# Register your models here.

@admin.register(Todolist)
class TodolistAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')  # Adjust as needed
