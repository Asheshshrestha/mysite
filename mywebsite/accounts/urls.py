from django.urls import path
from accounts.views import SignUpView
from django.contrib.auth.views import (LoginView,
                                        LogoutView,
                                        PasswordResetView,
                                        PasswordResetConfirmView,
                                        PasswordResetDoneView,
                                        PasswordResetCompleteView)

urlpatterns = [
    path('register/',SignUpView.as_view(),name='register'),
    path('login/',LoginView.as_view(template_name = 'dashboard/pages/account/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='dashboard/pages/account/logout.html'),name='logout')
]
