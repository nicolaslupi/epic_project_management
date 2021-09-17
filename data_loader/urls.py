""" DATA LOADER URLs """

from django.urls import path
from . import views

app_name = 'data_loader'

urlpatterns = [
    path('edit_component/<int:id>', views.edit_component, name='edit_component'),
    path('edit_system/<int:id>', views.edit_system, name='edit_system'),
    path('edit_project/<int:id>', views.edit_project, name='edit_project'),
    path('edit_person/<int:id>', views.edit_person, name='edit_person'),
    path('edit_supplier/<int:id>', views.edit_supplier, name='edit_supplier'),
    path('components/', views.components, name='components'),
    path('systems/', views.systems, name='systems'),
    path('projects/', views.projects, name='projects'),
    path('persons/', views.persons, name='persons'),
    path('suppliers/', views.suppliers, name='suppliers'),
    path('load_component/', views.load_component, name='load_component'),
    path('load_system/', views.load_system, name='load_system'),
    path('load_project/', views.load_project, name='load_project'),
    path('load_person/', views.load_person, name='load_person'),
    path('load_supplier/', views.load_supplier, name='load_supplier'),
    #path('ajax/load-stages/', views.load_stages, name='ajax_load_stages'), # AJAX
    path('ajax/load-systems/', views.load_systems, name='ajax_load_systems'), # AJAX
    path("get_components/", views.get_components.as_view()),
    path("get_systems/", views.get_systems.as_view()),
    path("get_projects/", views.get_projects.as_view()),
    path("get_persons/", views.get_persons.as_view()),
]