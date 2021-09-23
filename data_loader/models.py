""" DATA MODELS """
from django.db import models
#from definitions.models import Track, Stage

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    web = models.CharField(max_length=100, blank=True, null=True)
    mail = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Person(models.Model):
    full_name = models.CharField(max_length=100)
    area = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    mail = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.full_name

class Project(models.Model):
    name = models.CharField(max_length=100)
    #track = models.ForeignKey(Track, on_delete=models.SET_NULL, null=True)
    #stage = models.ForeignKey(Stage, on_delete=models.SET_NULL, null=True)
    #d_next = models.DateField(null=True)
    #d_done = models.DateField(null=True)
    #action = models.CharField(max_length=100, blank=True)
    #action_date = models.DateField(null=True, blank=True)
    depends_on = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    person = models.ManyToManyField(Person)

    def __str__(self):
        if self.depends_on:
            return self.name + ' - ' + self.depends_on.name
        else:
            return self.name

class System(models.Model):
    name = models.CharField(max_length=100)
    # track = models.ForeignKey(Track, on_delete=models.SET_NULL, null=True)
    # stage = models.ForeignKey(Stage, on_delete=models.SET_NULL, null=True)
    # d_next = models.DateField(null=True)
    # d_done = models.DateField(null=True)
    # action = models.CharField(max_length=100, blank=True)
    # action_date = models.DateField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    depends_on = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    person = models.ManyToManyField(Person)
    
    def __str__(self):
        if self.depends_on:
            return self.name + ' - ' + self.depends_on.name + ' - ' + self.project.name
        else:
            return self.name + ' - ' + self.project.name

class ItemType(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Item(models.Model):
    type = models.ForeignKey(ItemType, on_delete=models.SET_NULL, null=True)

    #type = models.ForeignKey(Atornillador, on_delete=models.SET_NULL, null=True)

    #subtype = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)
    comments = models.CharField(max_length=200, null=True, blank=True)
    # track = models.ForeignKey(Track, on_delete=models.SET_NULL, null=True)
    # stage = models.ForeignKey(Stage, on_delete=models.SET_NULL, null=True)
    # d_next = models.DateField(null=True)
    # d_done = models.DateField(null=True)
    # action = models.CharField(max_length=100, blank=True)
    # action_date = models.DateField(null=True, blank=True)
    load_date = models.DateField(null=True, blank=True)
    person = models.ManyToManyField(Person)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    system = models.ForeignKey(System, on_delete=models.SET_NULL, null=True, blank=True)
    supplied_by = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        title = self.type.name + ' - ' + self.project.name + ' - ' + self.system.name
        return title

# Van a tener un campo llamado item_ptr
class Atornillador(Item):
    RPM = models.IntegerField(blank=True, null=True)
    class Meta:
        verbose_name_plural = 'atornilladores'

class Capacitor(Item):
    capacitancia = models.IntegerField(blank=True, null=True)
    voltaje = models.IntegerField(blank=True, null=True)
    class Meta:
        verbose_name_plural = 'capacitores'