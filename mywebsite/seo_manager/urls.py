from os import name
from django.urls import path
from seo_manager.views import (seo_list,
                                page_list,
                                seo_tag_update,
                                add_seo_tag,
                                delete_seo_tag,
                                delete_seo_tag_confirm)

urlpatterns = [
    path('list',seo_list,name='seo_list'),
    path('update/<int:seo_id>/',seo_tag_update,name='seo_tag_update'),
    path('add/',add_seo_tag,name='add_seo_tag'),
    path('delete/<int:seo_id>/',delete_seo_tag,name='delete_seo_tag'),
    path('delete_confirm/<int:seo_id>/',delete_seo_tag_confirm,name='delete_seo_tag_confirm'),
    path('pages',page_list,name='page_list')
]
