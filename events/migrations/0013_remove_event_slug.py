# Generated by Django 5.0.1 on 2024-02-09 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_alter_todolist_name_alter_item_order_with_respect_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='slug',
        ),
    ]
