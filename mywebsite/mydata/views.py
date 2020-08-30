from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
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