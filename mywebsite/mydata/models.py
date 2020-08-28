from django.db import models
from faicon.fields import FAIconField
# Create your models here.

class PersonalData(models.Model):

    first_name = models.CharField(max_length=10,null=True)
    last_name = models.CharField(max_length=20,null=True)
    image = models.ImageField(null=True)
    carrer_status = models.CharField(max_length=30,null=True)
    short_desc = models.CharField(max_length=200,null=True)
    dob = models.DateField(null=True)
    phone = models.CharField(max_length=20)
    mail = models.EmailField(null=True)
    current_location = models.CharField(max_length=100,null=True)
    fb_link = models.URLField(null=True)
    tw_link = models.URLField(null=True)
    lin_link = models.URLField(null=True)

    def __str__(self):
        return self.first_name

class WorkCount(models.Model):

    work_name = models.CharField(max_length=20,null=True)
    count = models.CharField(max_length=10,null=True)
    icon = FAIconField()

    def __str__(self):
        return self.work_name

class Skills(models.Model):
    
    skill_name =models.CharField(max_length=30,null=True)
    percentage = models.CharField(max_length=2,null=True)

    def __str__(self):
        return self.skill_name

class AboutMyself(models.Model):

    short_desc = models.CharField(max_length=300,null=True)
    work_count = models.ManyToManyField(WorkCount,null=True)
    Skills = models.ManyToManyField(Skills,null=True)

    def __str__(self):
        return self.short_desc[:10]
