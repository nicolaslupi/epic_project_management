from django.contrib import admin
from .models import Item, System, Project, Person, Supplier, Atornillador, Capacitor
# Register your models here.

admin.site.register(Item)
#admin.site.register(ItemType)
admin.site.register(System)
admin.site.register(Project)
admin.site.register(Person)
admin.site.register(Supplier)
admin.site.register(Atornillador)
admin.site.register(Capacitor)