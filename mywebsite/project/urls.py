from django.urls import path,include
from project.views import project_list,update_project

urlpatterns = [
    path('list/',project_list,name='project_list'),
    path('update/<int:id>',update_project,name='update_project'),
]