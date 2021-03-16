from django.contrib import admin
from .models import Component, System, Project, Person, Supplier
# Register your models here.

admin.site.register(Component)
admin.site.register(System)
admin.site.register(Project)
admin.site.register(Person)
admin.site.register(Supplier)