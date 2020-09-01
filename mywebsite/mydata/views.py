from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from mydata.forms import UserIntroForm,AboutMyselfForm,SkillsForm
from mydata.models import PersonalData,AboutMyself,Skills
from django.contrib import messages
# Create your views here.

@login_required
def dashboard_index(request):

    template_name = 'dashboard/pages/index/index.html'

    return render(request,template_name=template_name)

@login_required
def members(request):
    template_name = 'dashboard/pages/workspace/member/member.html'
    user_obj = User.objects.all()
    query = request.GET.get("q")
    if query:
        user_obj = user_obj.filter(
            Q(username__icontains = query ) |
            Q(email__icontains = query) |
            Q(first_name__icontains = query) |
            Q(last_name__icontains = query)
        ).distinct()
    paginator = Paginator(user_obj,6)
    page = request.GET.get("page")
    user = paginator.get_page(page)
    context = {
        'users':user
    }
    return render(request,template_name,context)

@login_required
def general_setting(request):

    template_name = 'dashboard\pages\workspace\general\general.html'

    return render(request,template_name)

@login_required
def personal_info_setting(request):
    data = PersonalData.objects.first()
    template_name ='dashboard\pages\workspace\integration\intro_setting_page.html'
    if request.method == 'POST':
        form = UserIntroForm(data = request.POST,files=request.FILES,instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Personal data is updated')
            return redirect('personal_info')
    else:
        form = UserIntroForm(instance=data)

    return render(request,template_name,{'form':form,'data':data})

@login_required
def about_yourself_setting(request):
    
    data = AboutMyself.objects.first()
    template_name = 'dashboard\pages\workspace\integration\\about_yourself_setting_page.html'
    if request.method == 'POST':
        form = AboutMyselfForm(data = request.POST,files=request.FILES,instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,'Your About Yourself data is updated')
            return redirect('about_yourself')
    else:
        form = AboutMyselfForm(instance=data)

    return render(request,template_name,{'form':form,'data':data})


@login_required
def skills_list(request):

    template_name ='dashboard\pages\workspace\integration\skills\skills_list.html'
    skill_obj = Skills.objects.all()
    query = request.GET.get("q")
    if query:
        skill_obj = skill_obj.filter(
            Q(skill_name__icontains = query ) |
            Q(percentage__icontains = query) 
        ).distinct()
    paginator = Paginator(skill_obj,6)
    page = request.GET.get("page")
    skills = paginator.get_page(page)
    context = {
        'users':skills
    }
    return render(request,template_name,context)

@login_required
def update_skill(request,skills_no):

    template_name = 'dashboard\pages\workspace\integration\skills\skills_update.html'
    skill = Skills.objects.get(id = skills_no)
    form = SkillsForm(instance=skill)
    if request.method == 'POST':
        form = SkillsForm(data=request.POST,instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Skill data is updated')
            return redirect('skill_list')
    else:
        form = SkillsForm(instance=skill)

    return render(request,template_name,{'form':form})


@login_required
def delete_skill(request,skills_id):

    template_name = 'dashboard\pages\workspace\integration\skills\skills_delete.html'
    skill = Skills.objects.get(id=skills_id)
    context = {
        'data':skill
    }
    return render(request,template_name,context)

@login_required
def delete_skill_confirm(request,skills_id):

    template_name = 'dashboard\pages\workspace\integration\skills\skills_delete.html'
    skill = Skills.objects.get(id= skills_id)
    if skill is not None:
        skill.delete()
        messages.warning(request,'Your Skill is deleted')
        return redirect('skill_list')
    context = {
        'data':skill
    }
    return render(request,template_name,context)

@login_required
def add_skill(request):
    template_name = 'dashboard\pages\workspace\integration\skills\skills_update.html'

    form = SkillsForm()
    if request.method == 'POST':
        form = SkillsForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your new Skill is added')
            return redirect('skill_list')
    else:
        form = SkillsForm()

    return render(request,template_name,{'form':form})

        

    

