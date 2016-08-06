# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-06 12:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_auto_20160805_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='NormalBooking',
            fields=[
                ('booking_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rooms.Booking')),
                ('notes', models.CharField(blank=True, max_length=150)),
            ],
            bases=('rooms.booking',),
        ),
        migrations.CreateModel(
            name='SocietyBooking',
            fields=[
                ('booking_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rooms.Booking')),
                ('society_name', models.CharField(max_length=100)),
                ('event_name', models.CharField(blank=True, max_length=100)),
            ],
            bases=('rooms.booking',),
        ),
        migrations.RemoveField(
            model_name='booking',
            name='event',
        ),
    ]
