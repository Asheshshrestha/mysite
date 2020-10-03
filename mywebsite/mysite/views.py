from django.shortcuts import render
from project.models import ProjectName
from blog.models import BlogModel
from django.db.models import Count
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from mydata.models import (PersonalData,
                            AboutMyself,
                            Experience,
                            Education,
                            OfferToClient,
                            Testimonials)
from seo_manager.decorators import register_page
# Create your views here.
@register_page
def home(request):

    template_name="pages/index/index.html"
    prof_data = PersonalData.objects.first()
    about_data = AboutMyself.objects.first()
    education_data = Education.objects.all().order_by('-start_date')
    experience_data = Experience.objects.all().order_by('-start_date')
    offer_to_clients = OfferToClient.objects.first()
    project_list = ProjectName.objects.all()[:6]
    testimonials = Testimonials.objects.first()
    context = {
                'projects':project_list,
                'profile':prof_data,
                'about' : about_data,
                'experience':experience_data,
                'education':education_data,
                'offer':offer_to_clients,
                'testimonials':testimonials
                }
    return render(request,template_name,context=context)
@register_page
def aboutus(request):
    template_name = "pages/about_us/about-us.html"
    prof_data = PersonalData.objects.first()
    about_data = AboutMyself.objects.first()
    testimonials = Testimonials.objects.first()
    context = {
                'profile':prof_data,
                'about' : about_data,
                 'testimonials':testimonials
    }
    return render(request,template_name,context=context)
@register_page
def blogs(request):
    template_name = "pages/blogs/blog.html"
    blogs_obj = BlogModel.objects.all()
    query = request.GET.get("q")
    if query:
        blogs_obj = blogs_obj.filter(
            Q(title__icontains = query ) |
            Q(summary__icontains = query) |
            Q(category__icontains = query) 
        ).distinct()
    paginator = Paginator(blogs_obj,6)
    page = request.GET.get("page",1)
    try:
        blogs = paginator.get_page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    
    b_counts = BlogModel.objects.values('category').annotate(count=Count('category'))
    p_blogs = BlogModel.objects.all().order_by('-view_count')[:4]
    context = {
        'blogs':blogs,
        'b_counts':b_counts,
        'p_blog':p_blogs
    }
    return render(request,template_name,context)
@register_page
def contactus(request):
    template_name = "pages/contact_us/contact.html"
    return render(request,template_name)

@register_page
def services(request):
    template_name = "pages/services/services.html"
    offer_to_clients = OfferToClient.objects.first()
    testimonials = Testimonials.objects.first
    context = {
                'offer':offer_to_clients,
                'testimonials':testimonials
                }
    return render(request,template_name,context=context)

@register_page
def single_blog(request,blog_id):
    template_name = "pages/blogs/single_blog/single_blog.html"
    blog = BlogModel.objects.get(id= blog_id)
    b_counts = BlogModel.objects.values('category').annotate(count=Count('category'))
    p_blogs = BlogModel.objects.all().order_by('-view_count')[:4]
    if blog is not None:
        blog.view_count += 1
        blog.save()
    context = {
        'blog':blog,
        'b_counts':b_counts,
        'p_blog':p_blogs
    }
    return render(request,template_name,context)
    
@register_page
def projects(request):
    template_name = "pages/projects/projects.html"
    project_list = ProjectName.objects.all()
    context={
        'projects':project_list
    }
    return render(request,template_name,context)