from django.forms.widgets import NumberInput, Textarea
import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter
from django import forms
from .models import Compra, Item, Retiro, System
from definitions.models import ItemSubType

class DateInput(forms.DateInput):
    input_type = 'date'
    size=1

class ItemFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subtype'].queryset = ItemSubType.objects.none()

        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['subtype'].queryset = ItemSubType.objects.filter(item_type = type_id).order_by('name')
            except:
                pass
        else:
            self.fields['subtype'].queryset = ItemSubType.objects.none()
        
class ItemFilter(django_filters.FilterSet):
    supplier_pn = CharFilter(field_name='supplier_pn', lookup_expr='icontains', widget=Textarea(attrs= {'rows':1,'cols': 15 } ))
    manufacturer_pn = CharFilter(field_name='manufacturer_pn', lookup_expr='icontains', widget=Textarea(attrs= {'rows':1,'cols': 15 } ))
    start_date = DateFilter(field_name='compra__date', lookup_expr='gte', widget=DateInput())
    end_date = DateFilter(field_name='compra__date', lookup_expr='lte', widget=DateInput())
    unit_price = NumberFilter(field_name='unit_price', widget=NumberInput(attrs={'size':'10'}))
    description = CharFilter(field_name='description', lookup_expr='icontains', widget=Textarea(attrs= {'rows':1,'cols': 15 } ))
    link_compra = CharFilter(field_name='link_compra', lookup_expr='icontains', widget=Textarea(attrs= {'rows':1,'cols': 15 } ))
    link_datasheet = CharFilter(field_name='link_datasheet', lookup_expr='icontains', widget=Textarea(attrs= {'rows':1,'cols': 15 } ))

    class Meta:
        model = Item
        fields = ['compra','compra__supplier','type','subtype','manufacturer']
        form = ItemFilterForm


class RetiroFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['item__subtype'].queryset = ItemSubType.objects.none()
        if 'item__type' in self.data:
            try:
                type_id = int(self.data.get('item__type'))
                self.fields['item__subtype'].queryset = ItemSubType.objects.filter(item_type = type_id).order_by('name')
            except:
                pass
        else:
            self.fields['item__subtype'].queryset = ItemSubType.objects.none()

        self.fields['system'].queryset = System.objects.none()
        if 'project' in self.data:
            try:
                project_id = int(self.data.get('project'))
                self.fields['system'].queryset = System.objects.filter(project = project_id).order_by('name')
            except (ValueError, TypeError):
                pass
        else:
            self.fields['system'].queryset = System.objects.none()

class RetiroFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date', lookup_expr='gte', widget=DateInput())
    end_date = DateFilter(field_name='date', lookup_expr='lte', widget=DateInput())
    comentarios = CharFilter(field_name='comentarios', lookup_expr='icontains', widget=Textarea(attrs= {'rows':1,'cols': 15 } ))
    unidades = NumberFilter(field_name='unidades', widget=NumberInput(attrs={'size':'10'}))

    class Meta:
        model = Retiro
        fields = ['item','item__type', 'item__subtype', 'retirado_por','project','system']
        exclude = ['date']
        form = RetiroFilterForm


class CompraFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date', lookup_expr='gte', widget=DateInput())
    end_date = DateFilter(field_name='date', lookup_expr='lte', widget=DateInput())
    trello = CharFilter(field_name='trello', lookup_expr='icontains', widget=Textarea(attrs= {'rows':1,'cols': 15 } ))
    description = CharFilter(field_name='description', lookup_expr='icontains', widget=Textarea(attrs= {'rows':1,'cols': 15 } ))

    class Meta:
        model = Compra
        fields = '__all__'
        exclude = ['date']
