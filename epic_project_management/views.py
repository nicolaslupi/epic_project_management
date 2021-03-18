from django.http import HttpResponse
from django.shortcuts import render
from data_loader.models import *

def dependencies(root):
    aux = dict()
    sub_systems = System.objects.filter(depends_on = root.id)
    for system in sub_systems:
        aux[system] = dependencies(system)
    return aux

def home(request):
    projects = Project.objects.all()
    res = dict()
    for project in projects:
        assigned_systems = System.objects.filter(assigned_to_project = project.id, depends_on = None)
        aux = dict()
        for root in assigned_systems:
            aux[root] = dependencies(root)
        
        assigned_components = dict()
        for system in System.objects.all():
            assigned_components[system.name] = Component.objects.filter(assigned_to_system = system.id)
        res[project] = aux
    
    context = {
        'data':res,
        'assigned_components':assigned_components,
    }

    return render(request, 'homepage.html', context)
