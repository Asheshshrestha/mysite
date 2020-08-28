from django.shortcuts import render
from project.models import ProjectName
from mydata.models import PersonalData
# Create your views here.

def home(request):
    template_name="pages/index/index.html"
    prof_data = PersonalData.objects.first()
    project_list = ProjectName.objects.all()[:6]
    context = {
                'projects':project_list,
                'profile':prof_data
                }
    return render(request,template_name,context=context)

def aboutus(request):
    template_name = "pages/about_us/about-us.html"
    prof_data = PersonalData.objects.first()
    context = {
                'profile':prof_data
    }
    return render(request,template_name,context=context)

def blogs(request):
    template_name = "blog.html"
    return render(request,template_name)

def contactus(request):
    template_name = "pages/contact_us/contact.html"
    return render(request,template_name)

def services(request):
    template_name = "pages/services/services.html"
    return render(request,template_name)

def single_blog(request):
    template_name = "single-blog.html"
    return render(request,template_name)

def elements(request):
    template_name = "elements.html"
    return render(request,template_name)