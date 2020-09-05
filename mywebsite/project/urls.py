from django.urls import path,include
from project.views import project_list,update_project,delete_project,delete_project_confirm

urlpatterns = [
    path('list/',project_list,name='project_list'),
    path('update/<int:id>',update_project,name='update_project'),
    path('delete/<int:id>',delete_project,name='delete_project'),
    path('delete/confirm/<int:id>',delete_project_confirm,name='delete_project_confirm'),
]