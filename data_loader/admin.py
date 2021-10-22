from django.contrib import admin
from .models import Item, System, Project, Person, Supplier, Compra
# Register your models here.

admin.site.register(Item)
admin.site.register(Compra)
#admin.site.register(ItemType)
admin.site.register(System)
admin.site.register(Project)
admin.site.register(Person)
admin.site.register(Supplier)