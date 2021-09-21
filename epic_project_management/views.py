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

    root_projects = Project.objects.filter(depends_on = None)
    res = dict()
    #tags = dict()
    #stages = Stage.objects.all()
    #for stage in stages:
    #    tags[stage] = stage.tag
    
    for root_project in root_projects:
        assigned_projects = Project.objects.filter(depends_on = root_project.id)

        

    for project in projects:
        assigned_systems = System.objects.filter(project = project.id, depends_on = None)
        aux = {root: dependencies(root) for root in assigned_systems}
        res[project] = aux

    assigned_items = {system.name: Item.objects.filter(system=system.id) for system in System.objects.all()}
    
    context = {
        'data':res,
        'assigned_items':assigned_items,
        #'tags': tags,
    }

    return render(request, 'homepage.html', context)
