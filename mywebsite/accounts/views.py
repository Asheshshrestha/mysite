from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from accounts.forms import SignUpForm,UserUpadateForm,UserGroupForm
from django.views import View
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q


class SignUpView(View):
    @login_required
    def get(self, request, *args, **kwargs):
        template_name='dashboard/pages/account/register.html'
        form = SignUpForm()
        return render(request,template_name,{'form':form})
    @login_required
    def post(self, request, *args, **kwargs):
        #value = {'username':"",'email':"",'first_name':"",'last_name':"",'password1':"Ashesh1234",'password2':"Ashesh1234"}
        form = SignUpForm(request.POST)
        template_name='accounts/success.html'
        if form.is_valid():
            user =form.save(commit=False)
            raw_password = form.cleaned_data['password1']
            #raw_password =  User.objects.make_random_password(length=8, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889!@#$%^&*")
            username = form.cleaned_data['username']
            user.set_password(raw_password)
            user.save()
           
            return redirect('dashboard_index')

        else:
            return render(request, 'dashboard/pages/account/register.html', {'form':form})


        
@login_required
def create_group(request):
    template_name = 'dashboard/pages/account/group/create_group.html'
    if request.method == 'POST':
        form = UserGroupForm(data=request.POST)
        context = {
            'form':form
        }
        if form.is_valid():
            form.save()
            messages.success(
                request,'Successfully created new Group User'
            )
            return redirect('group_list')
        else:
            messages.warning(
                request,'Please submit valid form.'
            )
            return render(request,template_name,context)
    else:
        form = UserGroupForm()
        context ={
            'form':form
        }
        return render(request,template_name,context)


@login_required
def change_password(request):

    template_name = 'dashboard/pages/personal/security/change_password.html'
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('login')
        else:
            messages.warning(
                request, 'There was an error changing your password!')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, template_name, {'form': form}) 

@login_required
def user_update(request):

    template_name = 'dashboard/pages/personal/account/user_update.html'
    if request.method == 'POST':
        form = UserUpadateForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Your profile was updated.')
            return redirect('user_update')
    else:
        user = User.objects.get(username = request.user.username)
        form = UserUpadateForm(instance=user)
    
    return render(request,template_name,{'form':form})


@login_required
def group_list(request):

    template_name = 'dashboard/pages/account/group/group_list.html'
    group_obj = Group.objects.all()
    query = request.GET.get("q")
    if query:
        group_obj = group_obj.filter(
            Q(name__icontains = query )
        ).distinct()
    paginator = Paginator(group_obj,6)
    page = request.GET.get("page")
    groups = paginator.get_page(page)
    context = {
        'users':groups
    }
    return render(request,template_name,context)

@login_required
def update_group(request,grp_id):

    template_name = 'dashboard/pages/account/group/update_group.html'
    group = Group.objects.get(id= grp_id)
    form = UserGroupForm(instance=group)
    if request.method == 'POST':
        form = UserGroupForm(data = request.POST,instance=group)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Group data is updated')
            return redirect('group_list')
        else:
            messages.warning(request,'Submit a valid form')
            form = UserGroupForm(instance=group)
    else:
        form = UserGroupForm(instance=group)
    return render(request,template_name,{'form':form})

@login_required
def delete_group(request,grp_id):

    template_name = 'dashboard/pages/account/group/delete_group.html'
    group = Group.objects.get(id= grp_id)
    context = {
        'data':group
    }
    return render(request,template_name,context)

@login_required
def delete_group_confirm(request,grp_id):

    template_name = 'dashboard/pages/account/group/delete_group.html'
    group = Group.objects.get(id = grp_id)
    if group is not None:
        group.delete()
        messages.warning(request,'Group is Deleted')
        return redirect('group_list')
    context = {
                'data':group
    }
    return render(request,template_name,context)