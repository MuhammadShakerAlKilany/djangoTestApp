from django.db import models

# Create your models here.
class Item(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=255)
    count = models.IntegerField()