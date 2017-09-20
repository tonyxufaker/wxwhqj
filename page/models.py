# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    id = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50)