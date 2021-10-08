""" DEFINITIONS MODELS """
from django.db import models

class ItemType(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class ItemSubType(models.Model):
    name = models.CharField(max_length=100)
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

# class Track(models.Model):
#     name = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name

# class Stage(models.Model):
#     name = models.CharField(max_length=100)
#     track = models.ForeignKey(Track, on_delete=models.CASCADE)
#     tag = models.CharField(max_length=50, blank=True)
#     def __str__(self):
#         return self.name