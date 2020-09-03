
from django import forms
from mydata.models import (PersonalData
                            ,AboutMyself,
                            WorkCount,
                            Skills,
                            Education,
                            Experience)

class UserIntroForm(forms.ModelForm):
    
    class Meta:
        
        model = PersonalData
        widgets = { 'short_desc': forms.Textarea()}
        labels = {
        "fb_link": "Facebook Link",
        "tw_link": "Twitter Link",
        "lin_link": "Linkedin Link",
        "image":"Cover Image",
        "short_desc":"Short Description",
        "main":"Email Address",
        "phone":"Your Phone Number",
        "carrer_status":"Carrier Status",
        "dob":"Date of Birth"
    }
        fields = '__all__'


class AboutMyselfForm(forms.ModelForm):

    work_count = forms.ModelMultipleChoiceField(
        queryset= WorkCount.objects,
        widget = forms.CheckboxSelectMultiple
    )
    Skills = forms.ModelMultipleChoiceField(
        queryset= Skills.objects,
        widget = forms.CheckboxSelectMultiple
    )
    class Meta:

        model = AboutMyself
        widgets = { 'short_desc': forms.Textarea()}
        labels = {
            "work_count":"Work Tags",
            "short_desc":"Short Description",
            "Skills":"Your Skills"
        }
        fields = ('short_desc','work_count','Skills')

class SkillsForm(forms.ModelForm):

    class Meta:

        model = Skills
        fields = '__all__'

class WorkCountForm(forms.ModelForm):

    class Meta:
        model = WorkCount
        fields = '__all__'


class EducationForm(forms.ModelForm):

    class Meta:
         model = Education
         fields = '__all__'

class ExperienceForm(forms.ModelForm):

    class Meta:
        
        model = Experience
        fields = '__all__'