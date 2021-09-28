from django.http import HttpResponse
from django.shortcuts import render
from data_loader.models import *
from definitions.models import *

items_dict = {
    'Atornillador':Atornillador,
    'Capacitor':Capacitor,
    'Valvula':Valvula
}

def dependencies(root):
    aux = {system: dependencies(system) for system in System.objects.filter(parent = root.id)}
    return aux

def home(request):
    projects = Project.objects.all()

    root_projects = Project.objects.filter(parent = None)
    res = dict()
    #tags = dict()
    #stages = Stage.objects.all()
    #for stage in stages:
    #    tags[stage] = stage.tag
    
    for root_project in root_projects:
        assigned_projects = Project.objects.filter(parent = root_project.id)


    for project in projects:
        assigned_systems = System.objects.filter(project = project.id, parent = None)
        aux = {root: dependencies(root) for root in assigned_systems}
        res[project] = aux

    #assigned_items = {str(system.id) + '-' + system.name: Item.objects.filter(system=system.id) for system in System.objects.all()}
    assigned_items = {system.name: Item.objects.filter(system=system.id) for system in System.objects.all()}
    
    context = {
        'data':res,
        'assigned_items':assigned_items,
        #'tags': tags,
    }

    return render(request, 'homepage.html', context)




def project_dependencies(root):
    aux = {project: project_dependencies(project) for project in root.get_children()}
    return aux

def system_dependencies(root):
    aux = {system: system_dependencies(system) for system in root.get_children()}
    return aux

def test_tree(request):
    root_projects = Project.objects.filter(parent = None)
    projects_tree = {project: project_dependencies(project) for project in root_projects}

    systems_tree = dict()
    for project in Project.objects.all():
        assigned_systems = System.objects.filter(project = project.id, parent = None)
        aux = {root: system_dependencies(root) for root in assigned_systems}
        systems_tree[project] = aux

    assigned_items = {
            system: [items_dict[item.type].objects.get(item_ptr = item.pk) for item in Item.objects.filter(system=system.id)]
             for system in System.objects.all()
        }
    #assigned_items = {system: Item.objects.filter(system=system.id) for system in System.objects.all()}

    context = {
        'projects_tree': projects_tree,
        'systems_tree': systems_tree,
        'assigned_items': assigned_items
    }

    return render(request, 'test_home.html', context)