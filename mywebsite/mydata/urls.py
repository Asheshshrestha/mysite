from django.urls import path,include
from mydata.views import (dashboard_index,
                            members,
                            )

urlpatterns = [
    path('',dashboard_index,name='dashboard_index'),
    path('settings/workspace/members/',members,name='members')
]