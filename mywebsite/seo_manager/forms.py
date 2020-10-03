from django import forms
from django.db.models import fields
from seo_manager.models import SEOModel

class SEOTagForm(forms.ModelForm):

    class Meta:

        model = SEOModel
        fields = '__all__'