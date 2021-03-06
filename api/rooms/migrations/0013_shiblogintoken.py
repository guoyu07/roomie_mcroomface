# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-28 11:07
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0012_verifier'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShibLoginToken',
            fields=[
                ('sid', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('status', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shib_login_token', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
