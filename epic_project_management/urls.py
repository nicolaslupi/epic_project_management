""" MAIN URLs """

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data_loader/', include('data_loader.urls')),
    path('people/', include('people.urls')),
    path('', views.home),
]

