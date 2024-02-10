# Generated by Django 5.0.1 on 2024-02-10 08:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=150)),
                ('guest_number', models.IntegerField(default=10)),
                ('message', models.CharField()),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
