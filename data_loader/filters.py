from django.forms.widgets import Textarea
import django_filters
from django_filters import DateFilter, CharFilter
from django import forms
from .models import Item

class DateInput(forms.DateInput):
    input_type = 'date'
    size=1

class ItemFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='load_date', lookup_expr='gte', widget=DateInput())
    end_date = DateFilter(field_name='load_date', lookup_expr='lte', widget=DateInput())
    description = CharFilter(field_name='description', lookup_expr='icontains', widget=Textarea(attrs= {'rows':1,'cols': 15 } ))

    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['load_date','comments']