from django.urls import path,include
from mydata.views import (dashboard_index,
                            members,
                            general_setting,
                            personal_info_setting,
                            about_yourself_setting
                            )

urlpatterns = [
    path('',dashboard_index,name='dashboard_index'),
    path('settings/workspace/members/',members,name='members'),
    path('settings/workspace/general_setting/',general_setting,name='general_setting'),
    path('settings/workspace/integration/personal-info/',personal_info_setting,name='personal_info'),
    path('settings/workspace/integration/about-yourself/',about_yourself_setting,name='about_yourself'),
]