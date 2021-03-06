# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-18 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0002_auto_20170517_2107'),
        ('Order', '0004_auto_20170517_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorder',
            name='name',
            field=models.CharField(default='Null', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workorder',
            name='staff',
            field=models.ManyToManyField(null=True, to='Person.Staff'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='task_items',
            field=models.ManyToManyField(blank=True, null=True, to='Order.Task'),
        ),
    ]
