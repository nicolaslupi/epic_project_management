""" DATA LOADER VIEWS """
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import render, redirect
from . import forms
from definitions.models import Stage
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from datetime import datetime

from .filters import ItemFilter
from django.core.paginator import Paginator

def items(request):
    items_values = Item.objects.order_by('id')
    filtros = ItemFilter(request.GET, queryset=items_values)
    items_values = filtros.qs
    
    paginator = Paginator(items_values, 20)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    
    context = {
        'items':items_values,
        'page_obj':page_obj,
        'filtros':filtros
        }
    return render(request, 'data_loader/items.html', context)

def edit_item(request, id):
    item = Item.objects.get(pk=id)
    form = forms.CreateItem(request.POST or None, instance=item)
    if request.method == 'POST':
        form.save()
        return redirect('data_loader:items')
    else:
        return render(request, 'data_loader/edit_items.html', {'form':form})

# def load_item(request):
#     if request.method == 'POST':
#         form = forms.CreateItem(request.POST)
#         if form.is_valid():
#             repeat = request.POST['repeat']
#             if repeat == '':
#                 repeat = 1
#             else:
#                 repeat = int(repeat)
#             instance = form.save(commit=False)
#             for i in range(repeat):
#                 instance.pk = None
#                 if instance.load_date == None:
#                     instance.load_date = datetime.now().date()
#                 instance.save()
#                 form.save_m2m()
#             return redirect('data_loader:items')
#     else:
#         form = forms.CreateItem()
#     return render(request, 'data_loader/load_item.html', {'form':form})

def get_type(request):
    if request.method == 'POST':
        form = forms.GetItem(request.POST, list(forms_dict.keys()))
        if form.is_valid():
            type = request.POST['type']
            print(type)
            return load_item(request, ItemType.objects.get(pk=type).name)
    else:
        form = forms.GetItem()
    return render(request, 'data_loader/load_item.html', {'form':form})

forms_dict = {
    'Atornillador':forms.CreateAtornillador,
    'Capacitor':forms.CreateCapacitor
    }

def load_item(request, type):
    if request.method == 'POST':
        form = forms_dict[type](request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.type = type
            instance.pk = None
            if instance.load_date == None:
                instance.load_date = datetime.now().date()
            instance.save()
            form.save_m2m()
            return redirect('data_loader:items')    
    else:
        form = forms_dict[type]()
    return render(request, 'data_loader/load_item.html', {'form':form})


def systems(request):
    systems_values = System.objects.order_by('id')
    context = {'systems':systems_values}
    return render(request, 'data_loader/systems.html', context)

def edit_system(request, id):
    system = System.objects.get(pk=id)
    form = forms.CreateSystem(request.POST or None, instance=system)
    if request.method == 'POST':
        form.save()
        return redirect('data_loader:systems')
    else:
        return render(request, 'data_loader/edit_system.html', {'form':form})

def load_system(request):
    if request.method == 'POST':
        form = forms.CreateSystem(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_loader:systems')
    else:
        form = forms.CreateSystem()
    return render(request, 'data_loader/load_system.html', {'form':form})

def projects(request):
    projects_values = Project.objects.order_by('id')
    context = {'projects':projects_values}
    return render(request, 'data_loader/projects.html', context)

def edit_project(request, id):
    project = Project.objects.get(pk=id)
    form = forms.CreateProject(request.POST or None, instance=project)
    if request.method == 'POST':
        form.save()
        return redirect('data_loader:projects')
    else:
        return render(request, 'data_loader/edit_project.html', {'form':form})

def load_project(request):
    if request.method == 'POST':
        form = forms.CreateProject(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_loader:projects')
    else:
        form = forms.CreateProject()
    return render(request, 'data_loader/load_project.html', {'form':form})

def persons(request):
    persons_values = Person.objects.order_by('id')
    context = {'persons':persons_values}
    return render(request, 'data_loader/persons.html', context)

def edit_person(request, id):
    person = Person.objects.get(pk=id)
    form = forms.CreatePerson(request.POST or None, instance=person)
    if request.method == 'POST':
        form.save()
        return redirect('data_loader:persons')
    else:
        return render(request, 'data_loader/edit_person.html', {'form':form})

def load_person(request):
    if request.method == 'POST':
        form = forms.CreatePerson(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_loader:persons')
    else:
        form = forms.CreatePerson()
    return render(request,'data_loader/load_person.html', {'form':form})

def load_supplier(request):
    if request.method == 'POST':
        form = forms.CreateSupplier(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_loader:suppliers')
    else:
        form = forms.CreateSupplier()
    return render(request,'data_loader/load_supplier.html', {'form':form})

def edit_supplier(request, id):
    supplier = Supplier.objects.get(pk=id)
    form = forms.CreateSupplier(request.POST or None, instance=supplier)
    if request.method == 'POST':
        form.save()
        return redirect('data_loader:suppliers')
    else:
        return render(request, 'data_loader/edit_supplier.html', {'form':form})

def suppliers(request):
    suppliers_values = Supplier.objects.order_by('id')
    context = {'suppliers':suppliers_values}
    return render(request, 'data_loader/suppliers.html', context)

# AJAX
def load_systems(request):
    project_id = request.GET.get('project')
    systems = System.objects.filter(project = project_id).all()
    return render(request, 'data_loader/system_dropdown.html', {'systems': systems})

# def load_stages(request):
#     track_id = request.GET.get('track_id')
#     stages = Stage.objects.filter(track_id=track_id).all()
#     return render(request, 'data_loader/stage_dropdown.html', {'stages': stages})
#     # return JsonResponse(list(cities.values('id', 'name')), safe=False)

class get_items(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class get_systems(APIView):
    def get(self, request):
        systems = System.objects.all()
        serializer = SystemSerializer(systems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class get_projects(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class get_persons(APIView):
    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)