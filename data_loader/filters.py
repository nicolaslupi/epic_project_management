from django.forms.widgets import Textarea
import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class ItemFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='load_date', lookup_expr='gte', widget=Textarea(attrs= {'rows':1,'cols': 15 } ))
    end_date = DateFilter(field_name='load_date', lookup_expr='lte', widget=Textarea(attrs= {'rows':1,'cols': 15 } ))
    description = CharFilter(field_name='description', lookup_expr='icontains', widget=Textarea(attrs= {'rows':1,'cols': 15 } ))

    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['load_date','comments']