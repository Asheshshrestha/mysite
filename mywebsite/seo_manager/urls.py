from django.urls import path
from seo_manager.views import seo_list

urlpatterns = [
    path('list',seo_list,name='seo_list')
]
