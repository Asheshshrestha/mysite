from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from mydata.forms import UserIntroForm
from mydata.models import PersonalData
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
            return redirect('integration_setting')
    else:
        form = UserIntroForm(instance=data)

    return render(request,template_name,{'form':form,'data':data})

@login_required
def about_yourself_setting(request):
    
    template_name = 'dashboard\pages\workspace\integration\\about_yourself_setting_page.html'

    return render(request,template_name)