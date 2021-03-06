# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    num_pages = models.IntegerField()
    date_published = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title



# class Event(models.Model):
#   ...
#   #many-to-many with attendees
#   name = models.CharField(max_length=100)
#   date = models.DateField()
#
# class Attendee(models.Model):
#   ...
#   name = models.CharField(max_length=50)
#   events = models.ManyToManyField(Event)
#
# class Ticket(models.Model):
#   ...
#   #many-to-one
#   event = models.ForeignKey(Event, on_delete=models.CASCADE)
#   ticket_holder = models.ForeignKey(Attendee)
#   #through
