from django.urls import path,include
from mydata.views import (dashboard_index,
                            members,
                            general_setting,
                            integration_setting
                            )

urlpatterns = [
    path('',dashboard_index,name='dashboard_index'),
    path('settings/workspace/members/',members,name='members'),
    path('settings/workspace/general_setting/',general_setting,name='general_setting'),
    path('settings/workspace/integration_setting/',integration_setting,name='integration_setting'),
]