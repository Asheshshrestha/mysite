from django.urls import path
from accounts.views import SignUpView,change_password,user_update
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
    path('update/profile/',user_update,name='user_update')
]
