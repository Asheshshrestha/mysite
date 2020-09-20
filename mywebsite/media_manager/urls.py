from os import name
from django.urls import path,include
from media_manager.views import media_list,delete_media,delete_media_confirm,download_media

urlpatterns = [
    path('list',media_list,name='media_list'),
    path('delete/<str:img_id>/',delete_media,name='delete_media'),
    path('delete_confirm/',delete_media_confirm,name='delete_media_confirm'),
    path('download/<str:img_id>',download_media,name='download_media')
]
