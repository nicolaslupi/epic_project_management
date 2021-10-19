""" DATA LOADER VIEWS """
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import render, redirect
from . import forms
#from definitions.models import Stage
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from datetime import datetime

from .filters import ItemFilter
from django.core.paginator import Paginator


def load_type(request):
    if request.method == 'POST':
        form = forms.CreateType(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.pk = None
            
            instance.save()
            #return redirect('data_loader:items')    
            return load_item(request)
    else:
        form = forms.CreateType()
    return render(request, 'data_loader/load_type.html', {'form':form})


def load_purchase(request):
    if request.method == 'POST':
        form = forms.CreateCompra(request.POST)
        
        # Guardar compra y cargar Items, por ahora uno solo
        if form.is_valid():
            instance = form.save(commit=False)
            instance.pk = None

            instance.save()
            form.save_m2m()
            agregar = form.cleaned_data.get('agregar_items')
            
            if agregar:
                request.method = 'GET'
                return redirect('data_loader:load_item', compra=instance.pk)
            else:
                return redirect('data_loader:compras')
    else:
        form = forms.CreateCompra()
    return render(request, 'data_loader/load_purchase.html', {'form':form})

def compras(request):
    compras_values = Compra.objects.order_by('id')
    #filtros = RetiroFilter(request.GET, queryset=retiros_values)
    #retiros_values = filtros.qs
    
    paginator = Paginator(compras_values, 20)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    
    context = {
        'compras':compras_values,
        'page_obj':page_obj,
        #'filtros':filtros
        }
    return render(request, 'data_loader/compras.html', context)

def edit_compra(request, id):
    compra = Compra.objects.get(pk=id)
    form = forms.CreateCompra(request.POST or None, instance=compra)
    if request.method == 'POST':
        instance = form.save(commit=False)
        instance.save()

        agregar = form.cleaned_data.get('agregar_items')
            
        if agregar:
            request.method = 'GET'
            return redirect('data_loader:load_item', compra=instance.pk)
        else:
            return redirect('data_loader:compras')

    else:
        return render(request, 'data_loader/edit_compra.html', {'form':form})

def view_compra(request, id):
    selected_compra = Compra.objects.get(pk=id)
    items_values = Item.objects.filter(compra = selected_compra).order_by('id')

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
    #item = items_dict[type][1].objects.get(item_ptr = id)
    #form = items_dict[type][0](request.POST or None, instance = item)
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

# def get_type(request):
#     if request.method == 'POST':
#         form = forms.GetItem(request.POST)
#         if form.is_valid():
#             type = request.POST['type']
#             #return load_item(request, ItemType.objects.get(pk=type).name)
#             return load_item(request, type)
#     else:
#         form = forms.GetItem()
#     return render(request, 'data_loader/load_item.html', {'form':form})

def load_item(request, compra):
    if request.method=='POST':
        formset = forms.ItemFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form['type'].value():
                    child = form.save(commit=False)
                    child.compra = Compra.objects.get(pk = compra)
                    child.taken = 0
                    child.total_units = child.in_stock
                    
                    repeat = form.cleaned_data.get('repeat')
                    if repeat == '':
                        repeat = 1
                    else:
                        repeat = int(repeat)

                    for _ in range(repeat):
                        child.pk = None
                        child.save()

                    
                    #form.save_m2m()
                    #print(Compra.objects.get(pk=compra).loaded_by.all())
                    # if form.cleaned_data.get('asignar') == 'proyecto':
                    #     retiro = Retiro()
                    #     retiro.item = child
                    #     retiro.save()
                    #     for person in child.compra.loaded_by.all():
                    #         retiro.retirado_por.add(person.pk)
                        
                        #retiro.retirado_por

            return redirect('data_loader:items')
    else:
        formset = forms.ItemFormSet(queryset=Item.objects.none())
    return render(request, 'data_loader/load_item_formset.html', {'formset':formset})

def retirar_item(request, item):
    item = Item.objects.get(pk = item)
    in_stock = item.in_stock
    if request.method == 'POST':
        form = forms.RetirarItem(in_stock, request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            
            instance.item = item
            unidades = instance.unidades
            item.in_stock -= unidades
            item.taken += unidades
            item.save()
            instance.pk = None
            instance.save()
            return redirect('data_loader:items')
    else:
        form = forms.RetirarItem(in_stock)
    return render(request, 'data_loader/retirar_item.html', {'form':form})
        
def retiros(request):
    retiros_values = Retiro.objects.order_by('id')
    #filtros = RetiroFilter(request.GET, queryset=retiros_values)
    #retiros_values = filtros.qs
    
    paginator = Paginator(retiros_values, 20)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    
    context = {
        'retiros':retiros_values,
        'page_obj':page_obj,
        #'filtros':filtros
        }
    return render(request, 'data_loader/retiros.html', context)

""" Load Item Viejo """
# def load_item(request, compra):
#     print('\n\n',compra)
#     if request.method == 'POST':
#         form = forms.CreateItem(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             #instance.type = type
#             instance.compra = Compra.objects.get(pk = compra)
#             instance.pk = None
#             #if instance.load_date == None:
#             #    instance.load_date = datetime.now().date()
            
#             instance.save()
#             form.save_m2m()
#             return redirect('data_loader:items')    
#     else:
#         form = forms.CreateItem()
#     return render(request, 'data_loader/load_item.html', {'form':form})


def view_item(request, id):
    #item = items_dict[type][1].objects.get(item_ptr = id)
    item = Item.objects.get(pk = id)
    attrs = [(field.name.title(), getattr(item, field.name)) for field in item._meta.fields]
    #attrs.append( ('Person', ', '.join( [person.full_name for person in list(item.person.all())] )) )

    retiros = Retiro.objects.filter(item = id).order_by('id')

    paginator = Paginator(retiros, 20)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)

    context = {
        'attrs':attrs,
        'retiros':retiros,
        'page_obj':page_obj
        }

    return render(request, 'data_loader/view_item.html', context)
    
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

def view_system(request, id):
    selected_system = System.objects.get(pk=id)
    descendents = selected_system.get_descendants(include_self = True)
    items_values = Item.objects.filter(system__in = descendents).order_by('id')

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

def view_project(request, id):
    selected_project = Project.objects.get(pk=id)
    descendents = selected_project.get_descendants(include_self = True)
    items_values = Item.objects.filter(project__in = descendents).order_by('id')


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

def view_person(request, id):
    selected_person = Person.objects.get(pk=id)
    items_values = Item.objects.filter(person = selected_person).order_by('id')

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

def view_supplier(request, id):
    selected_supplier = Supplier.objects.get(pk=id)
    items_values = Item.objects.filter(supplied_by = selected_supplier).order_by('id')

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