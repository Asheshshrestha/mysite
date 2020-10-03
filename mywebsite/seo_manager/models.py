from django.db import models

class ActionModel(models.Model):

    action_name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.action_name
     

class SEOModel(models.Model):

    PAGE_TYPE_CHOOSE = (('front','front'),('dashboard','dashboard'))
    page = models.CharField(choices=PAGE_TYPE_CHOOSE,max_length=20)
    action = models.OneToOneField(ActionModel,on_delete=models.DO_NOTHING)
    seo_name = models.CharField(max_length=100)
    page_title = models.CharField(max_length=500,null=True)
    robots = models.CharField(max_length=1000,null=True)
    copyright = models.CharField(max_length=1000,null=True)
    summary = models.CharField(max_length=1000,null=True)
    keywords = models.CharField(max_length=1000,null=True)
    url = models.URLField(null=True)
    page_description = models.CharField(max_length=1000,null=True)
    page_image = models.ImageField(upload_to='seo_image')

    def __str__(self):
        return self.seo_name
