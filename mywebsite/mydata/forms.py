
from django import forms
from mydata.models import PersonalData

class UserIntroForm(forms.ModelForm):
    
    class Meta:
        model = PersonalData
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