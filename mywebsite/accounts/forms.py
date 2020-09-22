
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User,Group,Permission
from django.contrib.admin.widgets import FilteredSelectMultiple


class EmailValidation(forms.EmailField):
    def validate(self, value):
        try:
            User.objects.get(email=value)
            raise forms.ValidationError("Email already Exists")
        except User.DoesNotExist as e:
            pass

        except Exception as e:
            raise forms.ValidationError("Email already Exists")


class SignUpForm(UserCreationForm):
    email = EmailValidation(required=True)
    
    class Meta:
        model =User
        fields =('username',
                 'email',
                 'first_name',
                 'last_name',
                 'password1',
                 'password2',
                 'groups'
               
                 )
                 

class UserUpadateForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    is_staff = forms.BooleanField(widget=forms.CheckboxInput(attrs={'disable':'disable'}))
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'is_staff'
        )
class UserGroupForm(forms.ModelForm):

    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget = FilteredSelectMultiple('permissions',is_stacked=False,attrs={'rows':'2'})
    )
    class Media:
        css = {'all': ('/static/admin/css/widgets.css',), }
        js = ('/admin/jsi18n/',)

    class Meta:
        model = Group
        fields = '__all__'
    
        