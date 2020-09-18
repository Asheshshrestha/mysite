from blog.models import BlogModel
from django.shortcuts import render
from blog.forms import BlogForm
# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages

@login_required
def add_blog(request):
    template_name = 'dashboard/pages/workspace/general/blog/add_blog.html'

    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Your new  blog is added')
            return redirect('blog_list')
    else:
        form = BlogForm()

    return render(request,template_name,{'form':form})

@login_required
def blog_list(request):

    template_name ='dashboard/pages/workspace/general/blog/blog_list.html'
    blog_obj = BlogModel.objects.all()
    query = request.GET.get("q")
    if query:
        blog_obj = blog_obj.filter(
            Q(title__icontains = query ) 
        ).distinct()
    paginator = Paginator(blog_obj,6)
    page = request.GET.get("page")
    blog = paginator.get_page(page)
    context = {
        'users':blog
    }
    return render(request,template_name,context)


@login_required
def update_blog(request,blog_id):

    template_name = 'dashboard/pages/workspace/general/blog/blog_update.html'
    blog = BlogModel.objects.get(id = blog_id)
    form = BlogForm(instance=blog)
    if request.method == 'POST':
        form = BlogForm(data=request.POST,instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request,'Your blog is updated')
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)

    return render(request,template_name,{'form':form})

@login_required
def delete_blog(request,blog_id):

    template_name = 'dashboard/pages/workspace/general/blog/blog_delete.html'
    blog = BlogModel.objects.get(id=blog_id)
    context = {
        'data':blog
    }
    return render(request,template_name,context)

@login_required
def delete_blog_confirm(request,blog_id):

    template_name = 'dashboard/pages/workspace/general/blog/blog_delete.html'
    blog = BlogModel.objects.get(id= blog_id)
    if blog is not None:
        blog.delete()
        messages.warning(request,'Your Blog is deleted')
        return redirect('blog_list')
    context = {
        'data':blog
    }
    return render(request,template_name,context)