from django.contrib import admin
from .models import Item, System, Project, Person, Supplier, Compra, Retiro
# Register your models here.

admin.site.register(Compra)
admin.site.register(Item)
admin.site.register(Retiro)
admin.site.register(System)
admin.site.register(Project)
admin.site.register(Person)
admin.site.register(Supplier)