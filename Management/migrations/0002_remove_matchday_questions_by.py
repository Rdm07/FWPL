# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 07:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchday',
            name='Questions_By',
        ),
    ]
