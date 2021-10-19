from django.forms.widgets import NumberInput, Textarea
import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter
from django import forms
from .models import Item

class DateInput(forms.DateInput):
    input_type = 'date'
    size=1

class ItemFilter(django_filters.FilterSet):
    #start_date = DateFilter(field_name='load_date', lookup_expr='gte', widget=DateInput())
    #end_date = DateFilter(field_name='load_date', lookup_expr='lte', widget=DateInput())
    manufacturer_pn = CharFilter(field_name='manufacturer_pn', lookup_expr='icontains', widget=Textarea(attrs= {'rows':1,'cols': 15 } ))
    unit_price = NumberFilter(field_name='unit_price', widget=NumberInput(attrs={'size':'10'}))
    description = CharFilter(field_name='description', lookup_expr='icontains', widget=Textarea(attrs= {'rows':1,'cols': 15 } ))
    link_compra = CharFilter(field_name='link_compra', lookup_expr='icontains', widget=Textarea(attrs= {'rows':1,'cols': 15 } ))
    link_datasheet = CharFilter(field_name='link_datasheet', lookup_expr='icontains', widget=Textarea(attrs= {'rows':1,'cols': 15 } ))

    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['comments']