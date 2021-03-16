""" DATA LOADER FORMS """

from django import forms
from django.forms import ModelForm
from . import models
from definitions.models import Track, Stage

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

class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'

class CreateComponent(forms.ModelForm):
    repeat = forms.IntegerField()
    class Meta:
        model = models.Component
        fields = '__all__'
        
        widgets = {
                'd_next':DateTimeInput(),
                'd_done':DateTimeInput(),
                'action_date':DateTimeInput(),
            }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stage'].queryset = Stage.objects.none()

        if 'track' in self.data:
            try:
                track_id = int(self.data.get('track'))
                self.fields['stage'].queryset = Stage.objects.filter(track_id=track_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['stage'].queryset = self.instance.track.stage_set.order_by('name')

class CreateSystem(forms.ModelForm):
    class Meta:
        model = models.System
        fields = '__all__'
        widgets = {
                'd_next':DateTimeInput(),
                'd_done':DateTimeInput(),
                'action_date':DateTimeInput(),
            }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stage'].queryset = Stage.objects.none()

        if 'track' in self.data:
            try:
                track_id = int(self.data.get('track'))
                self.fields['stage'].queryset = Stage.objects.filter(track_id=track_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['stage'].queryset = self.instance.track.stage_set.order_by('name')

class CreateProject(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = '__all__'
        widgets = {
                'd_next':DateTimeInput(),
                'd_done':DateTimeInput(),
                'action_date':DateTimeInput(),
            }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stage'].queryset = Stage.objects.none()

        if 'track' in self.data:
            try:
                track_id = int(self.data.get('track'))
                self.fields['stage'].queryset = Stage.objects.filter(track_id=track_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['stage'].queryset = self.instance.track.stage_set.order_by('name')

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