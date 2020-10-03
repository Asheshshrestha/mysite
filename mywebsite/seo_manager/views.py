from django.contrib import messages
from django.forms.widgets import Select
from django.http import request
from mydata.models import Offers
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from django.core.paginator import Paginator
from seo_manager.models import ActionModel,SEOModel
from seo_manager.forms import SEOTagForm
# Create your views here.

def seo_list(request):

    template_name = 'dashboard\pages\seo_management\seo_list.html'
    seo_obj = SEOModel.objects.all()
    query = request.GET.get("q")
    if query:
        seo_obj = seo_obj.filter(
            Q(page__icontains = query) |
            Q(action__icontains = query) |
            Q(seo_name__icontains = query) |
            Q(page_title__icontains = query) |
            Q(bussiness_type__icontains = query) |
            Q(page_description__icontains = query) 
        ).distinct()
    paginator = Paginator(seo_obj,6)
    page = request.GET.get("page")
    seo = paginator.get_page(page)
    context = {
        'users':seo
    }

    return render(request,template_name,context)

def seo_tag_update(request,seo_id):

    template_name = 'dashboard/pages/seo_management/seo_update_tag.html'
    seo_tag = SEOModel.objects.get(id= seo_id)
    form = SEOTagForm(instance=seo_tag)
    if request.method == 'POST':
        form = SEOTagForm(data=request.POST,files=request.FILES,instance=seo_tag)
        if form.is_valid():
            form.save()
            messages.success(request,'Your SEO Tag is updated')
            return redirect('seo_list')
    else:
        form = SEOTagForm(instance=seo_tag)
    return render(request,template_name,{'form':form})

def add_seo_tag(request):

    template_name = 'dashboard/pages/seo_management/seo_add_tag.html'
    form = SEOTagForm()
    if request.method == 'POST':
        form = SEOTagForm(data = request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Your New SEO Tag is added successfully')
            return redirect('seo_list')
    else:
        form = SEOTagForm()
    return render(request,template_name,{'form':form})

def delete_seo_tag(request,seo_id):

    template_name = 'dashboard/pages/seo_management/delete_seo_tag.html'
    seo_tag = SEOModel.objects.get(id=seo_id)
    context = {
        'data':seo_tag
    }
    return render(request,template_name,context)

def delete_seo_tag_confirm(request,seo_id):

    template_name = 'dashboard/pages/seo_management/delete_seo_tag.html'
    seo_tag = SEOModel.objects.get(id=seo_id)
    if seo_tag is not None:
        seo_tag.delete()
        messages.warning(request,'Your SEO Tag is deleted')
        return redirect('seo_list')
    context = {
        'data':seo_tag
    }
    return render(request,template_name,context)

def page_list(request):

    template_name = 'dashboard/pages/seo_management/page_list.html'

    pages_obj = ActionModel.objects.all()
    query = request.GET.get("q")
    if query:
        pages_obj = pages_obj.filter(
            Q(action_name__icontains = query)
        ).distinct()
    paginator = Paginator(pages_obj,6)
    page = request.GET.get("page")
    pages = paginator.get_page(page)
    context = {
        'users':pages
    }


    return render(request,template_name,context)
