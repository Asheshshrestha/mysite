from django.db.models.aggregates import Count, Sum
from blog.models import BlogModel
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from project.models import ProjectName
from mydata.forms import (TestimonialMessageForm, UserIntroForm,
                            AboutMyselfForm,
                            SkillsForm,
                            WorkCountForm,
                            EducationForm,
                            ExperienceForm,
                            TestimonialsForm,
                            OffersForm,
                            OfferToClientForm)
from mydata.models import (PersonalData,
                            AboutMyself,
                            Skills, TestimonialMessage,
                            WorkCount,
                            Education,
                            Experience,
                            Testimonials,
                            OfferToClient,
                            Offers
                            )
from django.contrib import messages
# Create your views here.

@login_required
def dashboard_index(request):

    template_name = 'dashboard/pages/index/index.html'
    blog_count = BlogModel.objects.all().count()
    project_count = ProjectName.objects.all().count()
    view_count = BlogModel.objects.aggregate(Sum('view_count'))['view_count__sum']
    member_count = User.objects.all().count()
    context={
        'blog_count':blog_count,
        'project_count':project_count,
        'view_count':view_count,
        'member_count':member_count
    }
    return render(request,template_name=template_name,context=context)

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

    template_name = 'dashboard/pages/workspace/general/general.html'

    return render(request,template_name)

@login_required
def personal_info_setting(request):
    data = PersonalData.objects.first()
    template_name ='dashboard/pages/workspace/integration/intro_setting_page.html'
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
    template_name = 'dashboard/pages/workspace/integration/about_yourself_setting_page.html'
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

    template_name ='dashboard/pages/workspace/integration/skills/skills_list.html'
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

    template_name = 'dashboard/pages/workspace/integration/skills/skills_update.html'
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

    template_name = 'dashboard/pages/workspace/integration/skills/skills_delete.html'
    skill = Skills.objects.get(id=skills_id)
    context = {
        'data':skill
    }
    return render(request,template_name,context)

@login_required
def delete_skill_confirm(request,skills_id):

    template_name = 'dashboard/pages/workspace/integration/skills/skills_delete.html'
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
    template_name = 'dashboard/pages/workspace/integration/skills/skills_update.html'

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

    template_name ='dashboard/pages/workspace/integration/work_count/work_count_list.html'
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

    template_name = 'dashboard/pages/workspace/integration/work_count/work_count_update.html'
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

    template_name = 'dashboard/pages/workspace/integration/work_count/work_count_delete.html'
    work_count = WorkCount.objects.get(id=work_count_id)
    context = {
        'data':work_count
    }
    return render(request,template_name,context)


@login_required
def delete_work_count_confirm(request,work_count_id):

    template_name = 'dashboard/pages/workspace/integration/work_count/work_count_delete.html'
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
    template_name = 'dashboard/pages/workspace/integration/work_count/add_work_count.html'

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

    template_name ='dashboard/pages/workspace/integration/education/education_setting_page.html'
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

    template_name = 'dashboard/pages/workspace/integration/education/education_update.html'
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

    template_name = 'dashboard/pages/workspace/integration/education/education_delete.html'
    education = Education.objects.get(id=education_id)
    context = {
        'data':education
    }
    return render(request,template_name,context)

@login_required
def delete_education_confirm(request,education_id):

    template_name = 'dashboard/pages/workspace/integration/education/education_delete.html'
    education = Education.objects.get(id= education_id)
    if education is not None:
        education.delete()
        messages.warning(request,'Your Education Data is deleted')
        return redirect('education_list')
    context = {
        'data':education
    }
    return render(request,template_name,context)

@login_required
def add_education(request):
    template_name = 'dashboard/pages/workspace/integration/education/add_education.html'

    form = EducationForm()
    if request.method == 'POST':
        form = EducationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your new Education data is added')
            return redirect('education_list')
    else:
        form = EducationForm()

    return render(request,template_name,{'form':form})

@login_required
def experience_list(request):

    template_name ='dashboard/pages/workspace/integration/experience/experience_list.html'
    exp_obj = Experience.objects.all()
    query = request.GET.get("q")
    if query:
        exp_obj = exp_obj.filter(
            Q(job_title__icontains = query ) |
            Q(employee_type__icontains = query) |
            Q(company_name__icontains = query) |
            Q(company_location__icontains = query)
        ).distinct()
    paginator = Paginator(exp_obj,6)
    page = request.GET.get("page")
    exp = paginator.get_page(page)
    context = {
        'users':exp
    }
    return render(request,template_name,context)


@login_required
def update_experience(request,exp_id):

    template_name = 'dashboard/pages/workspace/integration/experience/experience_update.html'
    exp = Experience.objects.get(id = exp_id)
    form = ExperienceForm(instance=exp)
    if request.method == 'POST':
        form = ExperienceForm(data=request.POST,instance=exp)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Experience data is updated')
            return redirect('experience_list')
    else:
        form = ExperienceForm(instance=exp)

    return render(request,template_name,{'form':form})



@login_required
def delete_experience(request,exp_id):

    template_name = 'dashboard/pages/workspace/integration/experience/experience_delete.html'
    exp = Experience.objects.get(id=exp_id)
    context = {
        'data':exp
    }
    return render(request,template_name,context)

@login_required
def delete_experience_confirm(request,exp_id):

    template_name = 'dashboard/pages/workspace/integration/experience/experience_delete.html'
    exp = Experience.objects.get(id= exp_id)
    if exp is not None:
        exp.delete()
        messages.warning(request,'Your Experience Data is deleted')
        return redirect('experience_list')
    context = {
        'data':exp
    }
    return render(request,template_name,context)

@login_required
def add_experience(request):

    template_name = 'dashboard/pages/workspace/integration/experience/add_experience.html'

    form = ExperienceForm()
    if request.method == 'POST':
        form = ExperienceForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your new Experience data is added')
            return redirect('experience_list')
    else:
        form = ExperienceForm()

    return render(request,template_name,{'form':form})


@login_required
def testimonial_setting(request):
    
    data = Testimonials.objects.first()
    template_name = 'dashboard/pages/workspace/integration/testimonials_setting_page.html'
    if request.method == 'POST':
        form = TestimonialsForm(data = request.POST,instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Testimonials data is updated')
            return redirect('testimonial_setting')
    else:
        form = TestimonialsForm(instance=data)

    return render(request,template_name,{'form':form,'data':data})

@login_required
def testimonial_list(request):

    template_name ='dashboard/pages/workspace/integration/testimonials/testimonials_list.html'
    testimonial_obj = TestimonialMessage.objects.all()
    query = request.GET.get("q")
    if query:
        testimonial_obj = testimonial_obj.filter(
            Q(message__icontains = query ) |
            Q(name__icontains = query) 
        ).distinct()
    paginator = Paginator(testimonial_obj,6)
    page = request.GET.get("page")
    testimonial = paginator.get_page(page)
    context = {
        'users':testimonial
    }
    return render(request,template_name,context)

@login_required
def update_testimonial(request,tes_id):

    template_name = 'dashboard/pages/workspace/integration/testimonials/testimonial_update.html'
    education = TestimonialMessage.objects.get(id = tes_id)
    form = TestimonialMessageForm(instance=education)
    if request.method == 'POST':
        form = TestimonialMessageForm(data=request.POST,instance=education)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Testimonial data is updated')
            return redirect('testimonial_list')
    else:
        form = TestimonialMessageForm(instance=education)

    return render(request,template_name,{'form':form})


@login_required
def delete_testimonial(request,tes_id):

    template_name = 'dashboard/pages/workspace/integration/testimonials/testimonial_delete.html'
    education = TestimonialMessage.objects.get(id=tes_id)
    context = {
        'data':education
    }
    return render(request,template_name,context)

@login_required
def delete_testimonial_confirm(request,tes_id):

    template_name = 'dashboard/pages/workspace/integration/testimonials/testimonial_delete.html'
    education = TestimonialMessage.objects.get(id= tes_id)
    if education is not None:
        education.delete()
        messages.warning(request,'Your Tesimonial Data is deleted')
        return redirect('testimonial_list')
    context = {
        'data':education
    }
    return render(request,template_name,context)

@login_required
def add_testimonial(request):
    template_name = 'dashboard/pages/workspace/integration/testimonials/add_testimonial.html'

    form = TestimonialMessageForm()
    if request.method == 'POST':
        form = TestimonialMessageForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your new Testimonial data is added')
            return redirect('testimonial_list')
    else:
        form = TestimonialMessageForm()

    return render(request,template_name,{'form':form})

@login_required
def myoffer_setting(request):
    
    data = OfferToClient.objects.first()
    template_name = 'dashboard/pages/workspace/integration/offer_setting_page.html'
    if request.method == 'POST':
        form = OfferToClientForm(data = request.POST,instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,'Your data is updated')
            return redirect('myoffer_setting')
    else:
        form = OfferToClientForm(instance=data)

    return render(request,template_name,{'form':form,'data':data})



@login_required
def myoffer_list(request):

    template_name ='dashboard/pages/workspace/integration/offers/offer_list.html'
    offer_obj = Offers.objects.all()
    query = request.GET.get("q")
    if query:
        offer_obj = offer_obj.filter(
            Q(title__icontains = query ) |
            Q(short_desc__icontains = query) 
        ).distinct()
    paginator = Paginator(offer_obj,6)
    page = request.GET.get("page")
    offer = paginator.get_page(page)
    context = {
        'users':offer
    }
    return render(request,template_name,context)



@login_required
def update_myoffer(request,offer_id):

    template_name = 'dashboard/pages/workspace/integration/offers/offer_update.html'
    offer = Offers.objects.get(id = offer_id)
    form = OffersForm(instance=offer)
    if request.method == 'POST':
        form = OffersForm(data=request.POST,instance=offer)
        if form.is_valid():
            form.save()
            messages.success(request,'Your data is updated')
            return redirect('myoffer_list')
    else:
        form = OffersForm(instance=offer)

    return render(request,template_name,{'form':form})


@login_required
def delete_myoffer(request,offer_id):

    template_name = 'dashboard/pages/workspace/integration/offers/offer_delete.html'
    offer = Offers.objects.get(id=offer_id)
    context = {
        'data':offer
    }
    return render(request,template_name,context)

@login_required
def delete_myoffer_confirm(request,offer_id):

    template_name = 'dashboard/pages/workspace/integration/offers/offer_delete.html'
    offer = Offers.objects.get(id= offer_id)
    if offer is not None:
        offer.delete()
        messages.warning(request,'Your Data is deleted')
        return redirect('myoffer_list')
    context = {
        'data':offer
    }
    return render(request,template_name,context)

@login_required
def add_myoffer(request):
    template_name = 'dashboard/pages/workspace/integration/offers/add_offer.html'

    form = OffersForm()
    if request.method == 'POST':
        form = OffersForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your new  data is added')
            return redirect('myoffer_list')
    else:
        form = OffersForm()

    return render(request,template_name,{'form':form})


