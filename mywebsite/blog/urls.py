from django.urls import path,include
from blog.views import add_blog,blog_list


urlpatterns = [
    path('add/',add_blog,name='add_blog'),
    path('list/',blog_list,name='blog_list')
]