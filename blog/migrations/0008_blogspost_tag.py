# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-20 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20161102_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogspost',
            name='tag',
            field=models.CharField(default='python', max_length=20),
        ),
    ]
