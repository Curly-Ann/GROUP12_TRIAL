from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects_list_view, name='projects_list'),
    path('projects/create/', views.create_project_view, name='create_project'),
]