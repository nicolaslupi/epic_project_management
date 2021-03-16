""" DATA LOADER URLs """

from django.urls import path
from . import views

app_name = 'data_loader'

urlpatterns = [
    path('components/', views.components, name='components'),
    path('load_component/', views.load_component, name='load_component'),
    path('load_system/', views.load_system, name='load_system'),
    path('load_project/', views.load_project, name='load_project'),
    path('load_person/', views.load_person, name='load_person'),
    path('load_supplier/', views.load_supplier, name='load_supplier'),
    path('ajax/load-stages/', views.load_stages, name='ajax_load_stages'), # AJAX
    path("get_components/", views.get_components.as_view()),
    path("get_systems/", views.get_systems.as_view()),
    path("get_projects/", views.get_projects.as_view()),
    path("get_persons/", views.get_persons.as_view()),
]
