""" DATA MODELS """
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
#from definitions.models import Track, Stage
from definitions.models import ItemType, ItemSubType

ITEM_TYPES = [
    ('Atornillador','Atornillador'),
    ('Capacitor','Capacitor'),
    ('Valvula','Valvula')
]

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    web = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    mail = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

# class Manufacturer(models.Model):
#     name = models.CharField(max_length=100)
#     web = models.CharField(max_length=100, blank=True, null=True)
#     address = models.CharField(max_length=100, blank=True, null=True)
#     mail = models.CharField(max_length=100, blank=True, null=True)
#     phone = models.CharField(max_length=100, blank=True, null=True)

#     def __str__(self):
#         return self.name

class Person(models.Model):
    full_name = models.CharField(max_length=100)
    area = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    mail = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.full_name

class Project(MPTTModel):
    name = models.CharField(max_length=100)
    #track = models.ForeignKey(Track, on_delete=models.SET_NULL, null=True)
    #stage = models.ForeignKey(Stage, on_delete=models.SET_NULL, null=True)
    #d_next = models.DateField(null=True)
    #d_done = models.DateField(null=True)
    #action = models.CharField(max_length=100, blank=True)
    #action_date = models.DateField(null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    person = models.ManyToManyField(Person)

    class MPTTMeta:
        oreder_insertion_by = ['name']

    def __str__(self):
        return self.name
    #    if self.depends_on:
    #        return self.name + ' - ' + self.depends_on.name
    #    else:
    #        return self.name

class System(MPTTModel):
    name = models.CharField(max_length=100)
    # track = models.ForeignKey(Track, on_delete=models.SET_NULL, null=True)
    # stage = models.ForeignKey(Stage, on_delete=models.SET_NULL, null=True)
    # d_next = models.DateField(null=True)
    # d_done = models.DateField(null=True)
    # action = models.CharField(max_length=100, blank=True)
    # action_date = models.DateField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    person = models.ManyToManyField(Person)
    
    def __str__(self):
        return self.name
    #    if self.depends_on:
    #        return self.name + ' - ' + self.depends_on.name + ' - ' + self.project.name
    #    else:
    #        return self.name + ' - ' + self.project.name

# Llevo a definitions
# class ItemType(models.Model):
#    name = models.CharField(max_length=100)
#    def __str__(self):
#        return self.name

class Compra(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    loaded_by = models.ManyToManyField(Person)
    trello = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    gasto = models.FloatField(null=True, blank=True)

class Item(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(ItemType, on_delete=models.SET_NULL, null=True)
    subtype = models.ForeignKey(ItemSubType, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    comments = models.CharField(max_length=200, null=True, blank=True)
    manufacturer = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    manufacturer_pn = models.CharField(max_length=200, null=True, blank=True)
    link_compra = models.CharField(max_length=200, null=True, blank=True)
    link_datasheet = models.CharField(max_length=200, null=True, blank=True)
    unit_price = models.FloatField(null=True, blank=True)
    total_units = models.PositiveIntegerField(blank=True, null=True)
    in_stock = models.PositiveIntegerField(default=0, blank=True, null=True)
    taken = models.PositiveIntegerField(default=0, blank=True, null=True)

    #type = models.CharField(max_length=100, choices=ITEM_TYPES, blank=True, null=True)
    #type = models.ForeignKey(Atornillador, on_delete=models.SET_NULL, null=True)
    #subtype = models.CharField(max_length=100)
    
    def __str__(self):
        #title = self.type + ' - ' + self.project.name + ' - ' + self.system.name
        #tags = ['Material', 'Pulgadas', 'RPM', 'Capacitancia', 'Voltaje']
        #values = [self.material, self.pulgadas, self.RPM, self.capacitancia, self.voltaje]

        #info = [tag + ': ' + str(value) for tag, value in zip(tags, values) if value != None ]
        #title = str(self.pk) + ' - ' + self.type.name + ' - ' + ' - '.join(info)
        title = str(self.pk) + ' ' + self.type.name + ' ' + self.subtype.name
        return title
    
    
    # track = models.ForeignKey(Track, on_delete=models.SET_NULL, null=True)
    # stage = models.ForeignKey(Stage, on_delete=models.SET_NULL, null=True)
    # d_next = models.DateField(null=True)
    # d_done = models.DateField(null=True)
    # action = models.CharField(max_length=100, blank=True)
    # action_date = models.DateField(null=True, blank=True)
    #load_date = models.DateField(null=True, blank=True)
    #person = models.ManyToManyField(Person)
    #project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    #system = models.ForeignKey(System, on_delete=models.SET_NULL, null=True, blank=True)
    #supplied_by = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)

    # material = models.CharField(max_length=200, blank=True, null=True)
    # pulgadas = models.CharField(max_length=200, blank=True, null=True)
    # RPM = models.IntegerField(blank=True, null=True)
    # capacitancia = models.IntegerField(blank=True, null=True)
    # voltaje = models.IntegerField(blank=True, null=True)

class Retiro(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    retirado_por = models.ManyToManyField(Person)
    date = models.DateField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    system = models.ForeignKey(System, on_delete=models.SET_NULL, null=True, blank=True)
    comentarios = models.CharField(max_length=200, null=True, blank=True)
    unidades = models.IntegerField()

    def __str__(self):
        return self.item.type.name

# Van a tener un campo llamado item_ptr
# class Atornillador(Item):
#     RPM = models.IntegerField(blank=True, null=True)
#     class Meta:
#         verbose_name_plural = 'atornilladores'
#     def __str__(self):
#         return str(str(self.item_ptr)) + ' ' +  str(self.RPM)

# class Capacitor(Item):
#     capacitancia = models.IntegerField(blank=True, null=True)
#     voltaje = models.IntegerField(blank=True, null=True)
#     class Meta:
#         verbose_name_plural = 'capacitores'
#     def __str__(self):
#         return str(str(self.item_ptr)) + ' ' +  str(self.capacitancia) + ' - ' + str(self.voltaje)

# class Valvula(Item):
#     material = models.CharField(max_length=200, blank=True, null=True)
#     pulgadas = models.CharField(max_length=200, blank=True, null=True)
#     class Meta:
#         verbose_name_plural = 'valvulas'
#     def __str__(self):
#         return str(str(self.item_ptr)) + ' ' + str(self.material) + ' - ' + str(self.pulgadas)