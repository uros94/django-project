# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-19 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0016_profile_recommendedbooks'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
