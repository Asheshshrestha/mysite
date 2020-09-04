from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class BlogModel(models.Model):

    title = models.CharField(max_length=200,null= True)
    content = RichTextUploadingField()
    pub_date = models.DateField(auto_now_add=True)
