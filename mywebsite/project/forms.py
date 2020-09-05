from django import forms
from project.models import ProjectName


class ProjectForm(forms.ModelForm):

    class Meta:

        model = ProjectName
        fields='__all__'