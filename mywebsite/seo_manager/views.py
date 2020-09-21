from django.http.response import HttpResponse
from django.shortcuts import render
from mysite.urls import urlpatterns
# Create your views here.

def seo_list(request):

    template_name = 'dashboard\pages\seo_management\seo_list.html'

    return render(request,template_name)
