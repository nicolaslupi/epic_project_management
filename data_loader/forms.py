""" DATA LOADER FORMS """

from django import forms
from django.db.models.base import Model
#from django.forms import ModelForm
#from django.forms import modelformset_factory
from . import models
from .models import System, Project
from definitions.models import ItemSubType
from mptt.forms import TreeNodeChoiceField
from django.core.validators import MaxValueValidator, MinValueValidator

AREAS = [
    ('propulsion','Propulsion'),
    ('electronics','Electronics'),
    ('structures','Structures'),
]

ROLES = [
    ('lead','Lead'),
    ('eng','Eng'),
    ('mech','Mech'),
]

class DateInput(forms.DateInput):
    input_type = 'date'
    size=1

class GetItem(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = ['type']
        
class CreateType(forms.ModelForm):
    class Meta:
        model = models.ItemType
        fields = '__all__'

class CreateCompra(forms.ModelForm):
    agregar_items = forms.BooleanField(required=False, initial=True)
    
    class Meta:
        model = models.Compra
        fields = '__all__'
        widgets = {
            'date':DateInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['agregar_items'].widget.attrs.update({'class':'btn btn-default'})
        
            
ACCIONES = [('stock','A Stock'),
            ('proyecto','A Proyecto')]

""" Model Forms - Varios Items con una sola carga """
# Lo comentado es por si en la carga del item se lo quiere asignar ya a un proyecto
# De lo contrario hay que cargarlo inicialmente a stock y luego llevarlo a un proyecto
class CreateItem(forms.ModelForm):
    repeat = forms.IntegerField(required=False, help_text='Crea n entradas con n códigos')
    asignar = forms.ChoiceField(choices=ACCIONES, widget=forms.RadioSelect)
    project = forms.CharField(max_length=200, required=False, label='Project', widget=forms.Select())
    system = forms.CharField(max_length=200, required=False, label='System', widget=forms.Select())
    
    class Meta:
        model = models.Item
        fields = '__all__'
        exclude = ['compra', 'total_units', 'taken']
        help_texts = {
            'in_stock': 'Unidades asignadas a cada entrada (n por código)'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['in_stock'].label = 'Unidades'
        
        self.fields['subtype'].queryset = ItemSubType.objects.none()

        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['subtype'].queryset = ItemSubType.objects.filter(item_type = type_id).order_by('name')
            except:
                pass
        elif self.instance.pk:
            self.fields['subtype'].queryset = self.instance.type.subtype_set.order_by('name')

        self.fields['system'].queryset = System.objects.none()
        self.fields['project'] = TreeNodeChoiceField(queryset=Project.objects.all())
        self.fields['project'].required = False
        
        if 'project' in self.data:
            print('\n\nHHH')
            try:
                project_id = int(self.data.get('project'))
                self.fields['system'].queryset = System.objects.filter(project = project_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['system'].queryset = self.instance.project.system_set.order_by('name')
    
    def clean(self):
        cleaned_data = self.cleaned_data
        asignar = cleaned_data.get('asignar')
        proyecto = cleaned_data.get('project')
        if (asignar=='proyecto') and not proyecto:
            raise forms.ValidationError("Asignar a un proyecto válido o a stock")
        return cleaned_data

# ItemFormSet = modelformset_factory(
#     Item, form = CreateItem, extra=1
# )

class RetirarItem(forms.ModelForm):
    class Meta:
        model = models.Retiro
        fields = '__all__'
        exclude = ['item']
        widgets = {
            'date':DateInput()
        }

    def __init__(self, in_stock, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['unidades'] = forms.IntegerField(validators=[MaxValueValidator(in_stock)])

        self.fields['system'].queryset = System.objects.none()
        
        if 'project' in self.data:
            try:
                project_id = int(self.data.get('project'))
                self.fields['system'].queryset = System.objects.filter(project = project_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['system'].queryset = self.instance.project.system_set.order_by('name')

# class CreateItem(forms.ModelForm):
#     #repeat = forms.IntegerField(required=False)
    
#     class Meta:
#         model = models.Item
#         fields = '__all__'
#         exclude = ['compra']
        
#         widgets = {
#             #'load_date':DateInput(),
#             'description':forms.Textarea(attrs={'rows':1, 'cols':15}),
#             'comments':forms.Textarea(attrs={'rows':1, 'cols':15}),
#             #'person':forms.Textarea(attrs={'rows':1, 'cols':15})
#         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        # self.fields['system'].queryset = System.objects.none()
        
        # if 'project' in self.data:
        #     try:
        #         project_id = int(self.data.get('project'))
        #         self.fields['system'].queryset = System.objects.filter(project = project_id).order_by('name')
        #     except (ValueError, TypeError):
        #         pass
        # elif self.instance.pk:
        #     self.fields['system'].queryset = self.instance.project.system_set.order_by('name')
    
# class CreateAtornillador(forms.ModelForm):
#     class Meta:
#         model = models.Atornillador
#         fields = '__all__'
#         #exclude = ['type']
        
#         widgets = {
#             'load_date':DateInput(),
#             'description':forms.Textarea(attrs={'rows':1, 'cols':15}),
#             'comments':forms.Textarea(attrs={'rows':1, 'cols':15}),
#             #'person':forms.Textarea(attrs={'rows':1, 'cols':15})
#         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['project'] = TreeNodeChoiceField(queryset=Project.objects.all())
    
# class CreateCapacitor(forms.ModelForm):
#     class Meta:
#         model = models.Capacitor
#         fields = '__all__'
#         #exclude = ['type']

#         widgets = {
#             'load_date':DateInput(),
#             'description':forms.Textarea(attrs={'rows':1, 'cols':15}),
#             'comments':forms.Textarea(attrs={'rows':1, 'cols':15}),
#             #'person':forms.Textarea(attrs={'rows':1, 'cols':15})
#         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['project'] = TreeNodeChoiceField(queryset=Project.objects.all())

# class CreateValvula(forms.ModelForm):
#     class Meta:
#         model = models.Valvula
#         fields = '__all__'
#         #exclude = ['type']

#         widgets = {
#             'load_date':DateInput(),
#             'description':forms.Textarea(attrs={'rows':1, 'cols':15}),
#             'comments':forms.Textarea(attrs={'rows':1, 'cols':15}),
#             #'person':forms.Textarea(attrs={'rows':1, 'cols':15})
#         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['project'] = TreeNodeChoiceField(queryset=Project.objects.all())

class CreateSystem(forms.ModelForm):
    class Meta:
        model = models.System
        fields = '__all__'
        
        # widgets = {
        #         'd_next':DateInput(),
        #         'd_done':DateInput(),
        #         'action_date':DateInput(),
        #     }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project'] = TreeNodeChoiceField(queryset=Project.objects.all())
        self.fields['parent'].queryset = System.objects.none()

        if 'project' in self.data:
            try:
                project_id = int(self.data.get('project'))
                self.fields['parent'].queryset = System.objects.filter(project = project_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['parent'].queryset = self.instance.project.system_set.order_by('name')
        
        #self.fields['stage'].queryset = Stage.objects.none()

        # if 'track' in self.data:
        #     try:
        #         track_id = int(self.data.get('track'))
        #         self.fields['stage'].queryset = Stage.objects.filter(track_id=track_id).order_by('name')
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
        #     self.fields['stage'].queryset = self.instance.track.stage_set.order_by('name')

class CreateProject(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = '__all__'
        # widgets = {
        #         'd_next':DateInput(),
        #         'd_done':DateInput(),
        #         'action_date':DateInput(),
        #     }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['stage'].queryset = Stage.objects.none()

        # if 'track' in self.data:
        #     try:
        #         track_id = int(self.data.get('track'))
        #         self.fields['stage'].queryset = Stage.objects.filter(track_id=track_id).order_by('name')
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
        #     self.fields['stage'].queryset = self.instance.track.stage_set.order_by('name')

class CreatePerson(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = '__all__'
        widgets = {
            'area':forms.Select(choices=AREAS),
            'role':forms.Select(choices=ROLES),
        }
    
class CreateSupplier(forms.ModelForm):
    class Meta:
        model = models.Supplier
        fields = '__all__'