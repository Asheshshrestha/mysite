from django.urls import path,include
from mydata.views import dashboard_index,members

urlpatterns = [
    path('',dashboard_index,name='dashboard_index'),
    path('members/',members,name='members')
]