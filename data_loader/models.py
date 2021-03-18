""" DATA MODELS """
from django.db import models
from definitions.models import Track, Stage

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    web = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Person(models.Model):
    full_name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class Project(models.Model):
    name = models.CharField(max_length=100)
    track = models.ForeignKey(Track, on_delete=models.SET_NULL, null=True)
    stage = models.ForeignKey(Stage, on_delete=models.SET_NULL, null=True)
    d_next = models.DateField()
    d_done = models.DateField()
    action = models.CharField(max_length=100, blank=True)
    action_date = models.DateField(blank=True)
    assigned_to_person = models.ManyToManyField(Person)

    def __str__(self):
        return self.name

class System(models.Model):
    name = models.CharField(max_length=100)
    track = models.ForeignKey(Track, on_delete=models.SET_NULL, null=True)
    stage = models.ForeignKey(Stage, on_delete=models.SET_NULL, null=True)
    d_next = models.DateField()
    d_done = models.DateField()
    action = models.CharField(max_length=100, blank=True)
    action_date = models.DateField(blank=True)
    depends_on = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    assigned_to_person = models.ManyToManyField(Person)
    assigned_to_project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Component(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    subtype = models.CharField(max_length=100)
    comments = models.CharField(max_length=200, null=True, blank=True)
    track = models.ForeignKey(Track, on_delete=models.SET_NULL, null=True)
    stage = models.ForeignKey(Stage, on_delete=models.SET_NULL, null=True)
    d_next = models.DateField()
    d_done = models.DateField()
    action = models.CharField(max_length=100, blank=True)
    action_date = models.DateField(blank=True)
    assigned_to_person = models.ManyToManyField(Person)
    assigned_to_system = models.ForeignKey(System, on_delete=models.SET_NULL, null=True, blank=True)
    supplied_by = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        title = self.name + ' ' + self.type + ' ' + self.subtype + ' ' + self.assigned_to_system.name
        return title