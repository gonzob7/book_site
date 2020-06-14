# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.Charfield(max_length=100)
    num_pages = models.IntegerField()
    date_published = models.DateField()
