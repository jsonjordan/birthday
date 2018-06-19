# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Birthday(models.Model):
    date = models.DateTimeField('date')
    last_updated = models.DateTimeField('last updated')

class Person(models.Model):
    birthday = models.ForeignKey(Birthday)
    submit_date = models.DateTimeField('submit date')

