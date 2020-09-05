from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from project.models import ProjectName
from project.forms import ProjectForm
from django.contrib import messages
# Create your views here.

@login_required
def project_list(request):

    template_name ='dashboard\pages\workspace\general\projects\project_list.html'
    project_obj = ProjectName.objects.all()
    query = request.GET.get("q")
    if query:
        project_obj = project_obj.filter(
            Q(title__icontains = query ) 
        ).distinct()
    paginator = Paginator(project_obj,6)
    page = request.GET.get("page")
    project = paginator.get_page(page)
    context = {
        'users':project
    }
    return render(request,template_name,context)



@login_required
def update_project(request,offer_id):

    template_name = 'dashboard\pages\workspace\integration\offers\offer_update.html'
    offer = ProjectName.objects.get(id = offer_id)
    form = ProjectForm(instance=offer)
    if request.method == 'POST':
        form = ProjectForm(data=request.POST,instance=offer)
        if form.is_valid():
            form.save()
            messages.success(request,'Your data is updated')
            return redirect('myoffer_list')
    else:
        form = ProjectForm(instance=offer)

    return render(request,template_name,{'form':form})


@login_required
def delete_project(request,offer_id):

    template_name = 'dashboard\pages\workspace\integration\offers\offer_delete.html'
    offer = ProjectName.objects.get(id=offer_id)
    context = {
        'data':offer
    }
    return render(request,template_name,context)

@login_required
def delete_project_confirm(request,offer_id):

    template_name = 'dashboard\pages\workspace\integration\offers\offer_delete.html'
    offer = ProjectName.objects.get(id= offer_id)
    if offer is not None:
        offer.delete()
        messages.warning(request,'Your Data is deleted')
        return redirect('myoffer_list')
    context = {
        'data':offer
    }
    return render(request,template_name,context)

@login_required
def add_project(request):
    template_name = 'dashboard\pages\workspace\integration\offers\\add_offer.html'

    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your new  data is added')
            return redirect('myoffer_list')
    else:
        form = ProjectForm()

    return render(request,template_name,{'form':form})