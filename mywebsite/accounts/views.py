from django.shortcuts import redirect, render
from accounts.forms import SignUpForm
from django.views import View

# Create your views here.


class SignUpView(View):
    
    def get(self, request, *args, **kwargs):
        template_name='dashboard/pages/account/register.html'
        form = SignUpForm()
        return render(request,template_name,{'form':form})

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

