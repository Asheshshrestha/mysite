from django.urls import path,include
from blog.views import add_blog,blog_list,update_blog


urlpatterns = [
    path('add/',add_blog,name='add_blog'),
    path('list/',blog_list,name='blog_list'),
    path('update/<int:blog_id>',update_blog,name='update_blog'),
]