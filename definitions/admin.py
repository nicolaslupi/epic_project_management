from django.contrib import admin
#from .models import Track, Stage
from .models import ItemType, ItemSubType
# Register your models here.

admin.site.register(ItemType)
admin.site.register(ItemSubType)
#admin.site.register(Track)
#admin.site.register(Stage)