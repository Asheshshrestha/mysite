from django.urls import path,include
from mydata.views import (dashboard_index,
                            members,
                            general_setting,
                            personal_info_setting,
                            about_yourself_setting,
                            skills_list,
                            update_skill,
                            delete_skill,
                            delete_skill_confirm,
                            add_skill,
                            work_count_list,
                            update_work_count,
                            delete_work_count,
                            delete_work_count_confirm
                            )

urlpatterns = [
    path('',dashboard_index,name='dashboard_index'),
    path('settings/workspace/members/',members,name='members'),
    path('settings/workspace/general_setting/',general_setting,name='general_setting'),
    path('settings/workspace/integration/personal-info/',personal_info_setting,name='personal_info'),
    path('settings/workspace/integration/about-yourself/',about_yourself_setting,name='about_yourself'),
    path('settings/workspace/integration/about-yourself/skills',skills_list,name='skill_list'),
    path('settings/workspace/integration/about-yourself/work-counts',work_count_list,name='work_count_list'),
    path('settings/workspace/integration/about-yourself/skills/update/<int:skills_no>/',update_skill,name='update_skill'),
    path('settings/workspace/integration/about-yourself/work-counts/update/<int:work_count_id>/',update_work_count,name='update_work_count'),
    path('settings/workspace/integration/about-yourself/skills/add/',add_skill,name='add_skill'),
    path('settings/workspace/integration/about-yourself/skills/delete/<int:skills_id>/',delete_skill,name='delete_skill'),
    path('settings/workspace/integration/about-yourself/work-count/delete/<int:work_count_id>/',delete_work_count,name='delete_work_count'),
    path('settings/workspace/integration/about-yourself/skills/delete_confirm/<int:skills_id>/',delete_skill_confirm,name='delete_skill_confirm'),
    path('settings/workspace/integration/about-yourself/work-count/delete_confirm/<int:work_count_id>/',delete_work_count_confirm,name='delete_work_count_confirm'),
]