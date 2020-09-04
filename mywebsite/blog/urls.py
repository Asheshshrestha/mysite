from django.urls import path,include
from blog.views import add_blog


urlpatterns = [
    path('add/',add_blog,name='add_blog'),
]