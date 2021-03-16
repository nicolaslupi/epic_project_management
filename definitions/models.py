""" DEFINITIONS MODELS """
from django.db import models

class Track(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Stage(models.Model):
    name = models.CharField(max_length=100)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    def __str__(self):
        return self.name