# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 02:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0009_auto_20170524_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='date_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
