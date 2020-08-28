from django.db import models

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