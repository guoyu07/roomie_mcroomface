# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-04 10:54
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0011_auto_20160825_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verifier',
            fields=[
                ('user_id', models.IntegerField(default=180)),
                ('param', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
