from django.urls import path
from accounts.views import (SignUpView,
                                change_password,
                                user_update,
                                create_group,
                                group_list,
                                update_group,
                                delete_group,
                                delete_group_confirm,
                                create_user,
                                admin_user_update,
                                admin_delete_user,
                                admin_delete_user_confirm)
from django.contrib.auth.views import (LoginView,
                                        LogoutView,
                                        PasswordResetView,
                                        PasswordResetConfirmView,
                                        PasswordResetDoneView,
                                        PasswordResetCompleteView)

urlpatterns = [
    path('register/',SignUpView.as_view(),name='register'),
    path('login/',LoginView.as_view(template_name = 'dashboard/pages/account/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='dashboard/pages/account/logout.html'),name='logout'),
     path('password-reset/',
         PasswordResetView.as_view(
             template_name='dashboard/pages/account/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(
             template_name='dashboard/pages/account/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='dashboard/pages/account/password_reset_conform.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(
             template_name='dashboard/pages/account/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('change/password/',change_password,name='change_password'),
    path('update/profile/',user_update,name='user_update'),
    path('group/create/',create_group,name='create_group'),
    path('group/list/',group_list,name='group_list'),
    path('group/update/<int:grp_id>/',update_group,name='update_group'),
    path('group/delete/<int:grp_id>/',delete_group,name='delete_group'),
    path('group/delete_confirm/<int:grp_id>/',delete_group_confirm,name = 'delete_group_confirm'),
    path('user/create/',create_user,name ='create_user'),
    path('user/update/<int:user_id>/',admin_user_update,name='admin_user_update'),
    path('user/delete/<int:user_id>/',admin_delete_user,name='admin_delete_user'),
    path('user/delete_confirm/<int:user_id>/',admin_delete_user_confirm,name='admin_delete_user_confirm'),
    
]
