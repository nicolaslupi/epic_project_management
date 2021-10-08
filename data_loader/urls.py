""" DATA LOADER URLs """

from django.urls import path
from . import views

app_name = 'data_loader'

urlpatterns = [
    path('edit_item/<int:id>', views.edit_item, name='edit_item'),
    path('edit_system/<int:id>', views.edit_system, name='edit_system'),
    path('edit_project/<int:id>', views.edit_project, name='edit_project'),
    path('edit_person/<int:id>', views.edit_person, name='edit_person'),
    path('edit_supplier/<int:id>', views.edit_supplier, name='edit_supplier'),
    path('items/', views.items, name='items'),
    path('systems/', views.systems, name='systems'),
    path('projects/', views.projects, name='projects'),
    path('persons/', views.persons, name='persons'),
    path('suppliers/', views.suppliers, name='suppliers'),
    path('load_purchase/', views.load_purchase, name='load_purchase'),
    path('load_type/', views.load_type, name='load_type'),
    path('load_item/<int:compra>', views.load_item, name='load_item'),
    path('load_system/', views.load_system, name='load_system'),
    path('load_project/', views.load_project, name='load_project'),
    path('load_person/', views.load_person, name='load_person'),
    path('load_supplier/', views.load_supplier, name='load_supplier'),
    path('ajax/load-systems/', views.load_systems, name='ajax_load_systems'), # AJAX
    path("get_systems/", views.get_systems.as_view()),
    path("get_projects/", views.get_projects.as_view()),
    path("get_persons/", views.get_persons.as_view()),
    path('view_item/<int:id>', views.view_item, name='view_item'),
    path('view_project/<int:id>', views.view_project, name='view_project'),
    path('view_system/<int:id>', views.view_system, name='view_system'),
    path('view_supplier/<int:id>', views.view_supplier, name='view_supplier'),
    path('view_person/<int:id>', views.view_person, name='view_person'),
]