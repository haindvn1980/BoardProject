from django.contrib import admin
from django.db import models


# Register your models here.
class Board(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100)
