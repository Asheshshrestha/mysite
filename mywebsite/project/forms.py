from django import forms
from project.models import ProjectName


class ProjectForm(forms.ModelForm):

    class Meta:

        model = ProjectName
        fields = (
                    'title',
                    'sub_title',
                    'discription',
                    'project_url',
                    'cover_image',
                    'project_type'
        )