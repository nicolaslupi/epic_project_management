import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class ItemFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='load_date', lookup_expr='gte')
    end_date = DateFilter(field_name='load_date', lookup_expr='lte')
    description = CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['load_date']