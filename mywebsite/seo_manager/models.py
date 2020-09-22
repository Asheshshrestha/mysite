from django.db import models


class SEOModel(models.Model):

    PAGE_CHOICE = (('front','Front'),('admin','Admin'))
    ACTION_CHOICE = (('xyt','xyz'),('wxy','wsy'))
    page = models.CharField(max_length=20,choices=PAGE_CHOICE,null=True)
    action = models.CharField(max_length=30,choices=ACTION_CHOICE)
    seo_name = models.CharField(max_length=100)
    business_type = models.CharField(max_length=100,null=True)
    page_description = models.CharField(max_length=1000,null=True)
    page_image = models.ImageField(upload_to='seo_image')

    def __str__(self):
        return self.seo_name


    