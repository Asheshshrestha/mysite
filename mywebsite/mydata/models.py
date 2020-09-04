from django.db import models
from faicon.fields import FAIconField
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
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
    def save(self):
    
		#Opening the uploaded image
	    im = Image.open(self.image)

	    output = BytesIO()

		#Resize/modify the image
	    im = im.resize( (668,690) )

		#after modifications, save it to the output
	    im.save(output, format='JPEG', quality=100)
	    output.seek(0)

		#change the imagefield value to be the newley modifed image value
	    self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

	    super(PersonalData,self).save()

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

class Experience(models.Model):

    e_type = (('Full-time','Full-time'),
                ('Part-time','Part-time'),
                ('Self-employed','Self-employed'),
                ('Freelance','Freelance'),
                ('Contract','Contract'),
                ('Internship','Internship'),
                ('Apprenticeship','Apperenticeship'))
    job_title = models.CharField( max_length=50,null=True)
    employee_type = models.CharField(max_length=20,choices=e_type,null=True)
    company_name = models.CharField(max_length=100,null=True)
    company_location = models.CharField(max_length=200,null=True)
    current_working = models.BooleanField(default=False)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

class Education(models.Model):
    
    institute_name = models.CharField(max_length=200,null=True)
    level = models.CharField(max_length=200,null=True)
    institute_location = models.CharField(max_length=200,null=True)
    current_studying = models.BooleanField(default=False)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

class Offers(models.Model):
    icon = FAIconField()
    title = models.CharField(max_length=100,null=True)
    short_desc = models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.title

class OfferToClient(models.Model):

    heading = models.CharField(max_length=100,null=True)
    sub_desc = models.CharField(max_length=300,null=True)
    offers = models.ManyToManyField(Offers)

class TestimonialMessage(models.Model):

    star_choice = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))
    message = models.CharField(max_length=1000,null=True)
    name = models.CharField(max_length=50,null=True)
    stars = models.CharField(max_length=1,choices=star_choice)

    def __str__(self):
        return self.name

class Testimonials(models.Model):

    sub_desc = models.CharField(max_length=500,null=True)
    testimonials = models.ManyToManyField(TestimonialMessage)