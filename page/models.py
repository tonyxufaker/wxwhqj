# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class apply(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    selection = models.CharField(max_length=50)
    content = models.TextField()
