from django.shortcuts import render

# Create your views here.

def dashboard_index(request):

    template_name = 'dashboard/pages/index/index.html'

    return render(request,template_name=template_name)