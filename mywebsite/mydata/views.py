from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from mydata.forms import (UserIntroForm,
                            AboutMyselfForm,
                            SkillsForm,
                            WorkCountForm,
                            EducationForm)
from mydata.models import (PersonalData,
                            AboutMyself,
                            Skills,
                            WorkCount,
                            Education)
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

        

    
@login_required
def work_count_list(request):

    template_name ='dashboard\pages\workspace\integration\work_count\work_count_list.html'
    work_count_obj = WorkCount.objects.all()
    query = request.GET.get("q")
    if query:
        work_count_obj = work_count_obj.filter(
            Q(skill_name__icontains = query ) |
            Q(percentage__icontains = query) 
        ).distinct()
    paginator = Paginator(work_count_obj,6)
    page = request.GET.get("page")
    work_counts = paginator.get_page(page)
    context = {
        'users':work_counts
    }
    return render(request,template_name,context)


@login_required
def update_work_count(request,work_count_id):

    template_name = 'dashboard\pages\workspace\integration\work_count\work_count_update.html'
    work_count = WorkCount.objects.get(id = work_count_id)
    form = WorkCountForm(instance=work_count)
    if request.method == 'POST':
        form = WorkCountForm(data=request.POST,instance=work_count)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Work Count data is updated')
            return redirect('work_count_list')
    else:
        form = WorkCountForm(instance=work_count)

    return render(request,template_name,{'form':form})


@login_required
def delete_work_count(request,work_count_id):

    template_name = 'dashboard\pages\workspace\integration\work_count\work_count_delete.html'
    work_count = WorkCount.objects.get(id=work_count_id)
    context = {
        'data':work_count
    }
    return render(request,template_name,context)


@login_required
def delete_work_count_confirm(request,work_count_id):

    template_name = 'dashboard\pages\workspace\integration\work_count\work_count_delete.html'
    work_count = WorkCount.objects.get(id= work_count_id)
    if work_count is not None:
        work_count.delete()
        messages.warning(request,'Your Work Count Data is deleted')
        return redirect('work_count_list')
    context = {
        'data':work_count
    }
    return render(request,template_name,context)

@login_required
def add_work_count(request):
    template_name = 'dashboard\pages\workspace\integration\work_count\\add_work_count.html'

    form = WorkCountForm()
    if request.method == 'POST':
        form = WorkCountForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your new Work Count is added')
            return redirect('work_count_list')
    else:
        form = WorkCountForm()

    return render(request,template_name,{'form':form})


@login_required
def education_list(request):

    template_name ='dashboard\pages\workspace\integration\education\education_setting_page.html'
    education_obj = Education.objects.all()
    query = request.GET.get("q")
    if query:
        education_obj = education_obj.filter(
            Q(institute_name__icontains = query ) |
            Q(level__icontains = query) |
            Q(institute_location__icontains = query)
        ).distinct()
    paginator = Paginator(education_obj,6)
    page = request.GET.get("page")
    educations = paginator.get_page(page)
    context = {
        'users':educations
    }
    return render(request,template_name,context)



@login_required
def update_education(request,education_id):

    template_name = 'dashboard\pages\workspace\integration\education\education_update.html'
    education = Education.objects.get(id = education_id)
    form = EducationForm(instance=education)
    if request.method == 'POST':
        form = EducationForm(data=request.POST,instance=education)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Education data is updated')
            return redirect('education_list')
    else:
        form = EducationForm(instance=education)

    return render(request,template_name,{'form':form})


@login_required
def delete_education(request,education_id):

    template_name = 'dashboard\pages\workspace\integration\education\education_delete.html'
    education = Education.objects.get(id=education_id)
    context = {
        'data':education
    }
    return render(request,template_name,context)

@login_required
def delete_education_confirm(request,education_id):

    template_name = 'dashboard\pages\workspace\integration\education\education_delete.html'
    education = Education.objects.get(id= education_id)
    if education is not None:
        education.delete()
        messages.warning(request,'Your Education Data is deleted')
        return redirect('education_list')
    context = {
        'data':education
    }
    return render(request,template_name,context)