from django import forms
from blog.models import BlogModel

class BlogForm(forms.ModelForm):
    
    class Meta:

        model = BlogModel
        fields = (
                    'title',
                    'cover_image',
                    'summary',
                    'category',
                    'content'
        )