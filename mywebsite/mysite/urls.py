"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from mysite.views import aboutus,contactus,services,blogs,single_blog,projects

urlpatterns = [
   path('about/',aboutus,name="aboutus"),
   path('contact/',contactus,name="contactus"),
   path('services/',services,name="services"),
   path('c-blog/',include('blog.urls')),
   path('c-project/',include('project.urls')),
   path('blog/',blogs,name='blogs'),
   path('projects/',projects,name='projects'),
   path('blog/detail/<int:blog_id>/',single_blog,name='blog_detail'),

]
