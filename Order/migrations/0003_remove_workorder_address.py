# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-17 20:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_auto_20170517_0425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workorder',
            name='address',
        ),
    ]