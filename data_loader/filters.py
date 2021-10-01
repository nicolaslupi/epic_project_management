from django.forms.widgets import NumberInput, Textarea
import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter
from django import forms
from .models import Item

class DateInput(forms.DateInput):
    input_type = 'date'
    size=1

class ItemFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='load_date', lookup_expr='gte', widget=DateInput())
    end_date = DateFilter(field_name='load_date', lookup_expr='lte', widget=DateInput())
    manufacturer_pn = CharFilter(field_name='manufacturer_pn', lookup_expr='icontains', widget=Textarea(attrs= {'rows':1,'cols': 15 } ))
    unit_price = NumberFilter(field_name='unit_price', widget=NumberInput(attrs={'size':'10'}))
    description = CharFilter(field_name='description', lookup_expr='icontains', widget=Textarea(attrs= {'rows':1,'cols': 15 } ))
    material = CharFilter(field_name='material', lookup_expr='icontains', widget=Textarea(attrs= {'rows':1,'cols': 15 } ))
    pulgadas = CharFilter(field_name='pulgadas', lookup_expr='icontains', widget=Textarea(attrs= {'rows':1,'cols': 15 } ))
    RPM = NumberFilter(field_name='RPM', widget=NumberInput(attrs={'size':'10'}))
    capacitancia = NumberFilter(field_name='capacitancia', widget=NumberInput(attrs={'size':'10'}))
    voltaje = NumberFilter(field_name='voltaje', widget=NumberInput(attrs={'size':'10'}))


    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['load_date','comments']