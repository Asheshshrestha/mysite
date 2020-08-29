from django.urls import path,include
from mydata.views import dashboard_index

urlpatterns = [
    path('',dashboard_index,name='dashboard_index')
]