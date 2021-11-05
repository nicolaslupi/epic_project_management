""" DEFINITIONS MODELS """
from django.db import models

class ItemType(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class ItemSubType(models.Model):
    name = models.CharField(max_length=100)
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    prefix = models.CharField(max_length=4, unique=True, null=True, blank=True)
    def __str__(self):
        return self.name
