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
                            delete_work_count_confirm,
                            add_work_count,
                            education_list,
                            update_education,
                            delete_education,
                            delete_education_confirm,
                            add_education,
                            experience_list,
                            update_experience,
                            delete_experience,
                            delete_experience_confirm
                            )

urlpatterns = [
    path('',dashboard_index,name='dashboard_index'),
    path('settings/workspace/members/',members,name='members'),
    path('settings/workspace/general_setting/',general_setting,name='general_setting'),
    path('settings/workspace/integration/personal-info/',personal_info_setting,name='personal_info'),
    path('settings/workspace/integration/about-yourself/',about_yourself_setting,name='about_yourself'),
    path('settings/workspace/integration/about-yourself/skills',skills_list,name='skill_list'),
    path('settings/workspace/integration/about-yourself/work-counts',work_count_list,name='work_count_list'),
    path('settings/workspace/integration/Education/',education_list,name='education_list'),
    path('settings/workspace/integration/Experience/',experience_list,name='experience_list'),
    path('settings/workspace/integration/about-yourself/skills/update/<int:skills_no>/',update_skill,name='update_skill'),
    path('settings/workspace/integration/Education/<int:education_id>/',update_education,name='update_education'),
    path('settings/workspace/integration/Experience/<int:exp_id>/',update_experience,name='update_experience'),
    path('settings/workspace/integration/about-yourself/work-counts/update/<int:work_count_id>/',update_work_count,name='update_work_count'),
    path('settings/workspace/integration/about-yourself/skills/add/',add_skill,name='add_skill'),
    path('settings/workspace/integration/about-yourself/work-count/add/',add_work_count,name='add_work_count'),
    path('settings/workspace/integration/Education/add/',add_education,name='add_education'),
    path('settings/workspace/integration/about-yourself/skills/delete/<int:skills_id>/',delete_skill,name='delete_skill'),
    path('settings/workspace/integration/Education/delete/<int:education_id>/',delete_education,name='delete_education'),
    path('settings/workspace/integration/Experience/delete/<int:exp_id>/',delete_experience,name='delete_experience'),
    path('settings/workspace/integration/about-yourself/work-count/delete/<int:work_count_id>/',delete_work_count,name='delete_work_count'),
    path('settings/workspace/integration/about-yourself/skills/delete_confirm/<int:skills_id>/',delete_skill_confirm,name='delete_skill_confirm'),
    path('settings/workspace/integration/about-yourself/work-count/delete_confirm/<int:work_count_id>/',delete_work_count_confirm,name='delete_work_count_confirm'),
    path('settings/workspace/integration/Education/delete_confirm/<int:education_id>/',delete_education_confirm,name='delete_education_confirm'),
    path('settings/workspace/integration/Experience/delete_confirm/<int:exp_id>/',delete_experience_confirm,name='delete_experience_confirm'),
]