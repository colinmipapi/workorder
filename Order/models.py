from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class WorkOrder(models.Model):
    name = models.CharField(max_length=200)
    staff = models.ManyToManyField(
        'Person.Staff',
        null = True,
    )
    task_items = models.ManyToManyField(
        'Order.Task',
        null = True,
        blank = True,
    )
    unit = models.ForeignKey(
        'Property.Unit',
        null = True,
    )

class Task(models.Model):

    TYPE = (
        ("D","Drywall"),
        ("E","Electrical"),
        ("P","Painting"),
        ("PG","Plumbing"),
        ("PL","Plaster"),
        ("R","Replacement"),
        ("A","Appliance"),
    )
    room = models.ManyToManyField(
        'Property.Room',
        null = True,
        blank= True,
    )
    item = models.ManyToManyField(
        'Property.Item',
        null = True,
        blank= True,
    )
    task_type = models.CharField(
        max_length = 1,
        choices = TYPE,
        null=True
    )
    vendor = models.ForeignKey(
        'Person.Vendor',
        blank = True,
        null = True,
    )
    staff = models.ManyToManyField(
        'Person.Staff',
        null = True,
    )
    description = models.TextField(null=True)
    review = models.ManyToManyField(
        'Order.Review',
        null= True,
        )


class Review(models.Model):

    date_time = models.DateTimeField(default=timezone.now,null=True)
    description = models.TextField(null=True)