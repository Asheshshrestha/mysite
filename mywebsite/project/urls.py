from django.urls import path,include
from project.views import project_list

urlpatterns = [
    path('list/',project_list,name='project_list')
]