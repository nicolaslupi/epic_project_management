from django.http import HttpResponse
from django.shortcuts import render
from data_loader.models import *
from definitions.models import *

def dependencies(root):
    aux = dict()
    sub_systems = System.objects.filter(depends_on = root.id)
    for system in sub_systems:
        aux[system] = dependencies(system)
    return aux

def home(request):
    projects = Project.objects.all()
    res = dict()
    tags = dict()
    #stages = Stage.objects.all()
    #for stage in stages:
    #    tags[stage] = stage.tag

    for project in projects:
        assigned_systems = System.objects.filter(project = project.id, depends_on = None)
        aux = dict()
        for root in assigned_systems:
            aux[root] = dependencies(root)
        
        
        assigned_items = {system.name: Item.objects.filter(system=system.id) for system in System.objects.all()}
        
        # assigned_items = dict()
        # for system in System.objects.all():
        #     assigned_items[system.name] = Item.objects.filter(assigned_to_system = system.id)
        res[project] = aux
    
    context = {
        'data':res,
        'assigned_items':assigned_items,
        'tags': tags,
    }

    return render(request, 'homepage.html', context)
