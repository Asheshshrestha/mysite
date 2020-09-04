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
    template_name = 'dashboard\pages\workspace\general\\blog\\add_blog.html'

    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your new  blog is added')
            return redirect('myoffer_list')
    else:
        form = BlogForm()

    return render(request,template_name,{'form':form})

@login_required
def blog_list(request):

    template_name ='dashboard\pages\workspace\general\\blog\\blog_list.html'
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