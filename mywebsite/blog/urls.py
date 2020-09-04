from django.urls import path,include
from blog.views import add_blog,blog_list,update_blog,delete_blog,delete_blog_confirm


urlpatterns = [
    path('add/',add_blog,name='add_blog'),
    path('list/',blog_list,name='blog_list'),
    path('update/<int:blog_id>',update_blog,name='update_blog'),
    path('delete/<int:blog_id>',delete_blog,name='delete_blog'),
    path('delete_confirm/<int:blog_id>',delete_blog_confirm,name='delete_blog_confirm')
]