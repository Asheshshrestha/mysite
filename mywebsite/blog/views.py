from django.shortcuts import render
from blog.forms import BlogForm
# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages

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