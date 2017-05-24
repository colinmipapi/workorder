# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 02:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0008_task_stage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_completed', models.DateTimeField()),
                ('complete', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='sub_task',
            field=models.ManyToManyField(blank=True, to='Order.Subtask'),
        ),
    ]
