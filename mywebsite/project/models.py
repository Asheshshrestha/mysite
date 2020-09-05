from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

# Create your models here.


class ProjectName(models.Model):
    
    type_choose=(('hardware','hardware'),('DjangoWebpage','DjangoWebpage'),('logo','logo'),('Diy','Diy'),('Desktop','Desktop'))
    title = models.CharField(max_length=225)
    sub_title = models.CharField(max_length=225)
    discription = models.TextField(null=True)
    view_count = models.IntegerField(default=0)
    uploaded = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    project_url = models.URLField(null=True)
    cover_image = models.ImageField(null=True)
    project_type =models.CharField(max_length=16,choices=type_choose)
    def save(self):
    
		#Opening the uploaded image
	    im = Image.open(self.cover_image)

	    output = BytesIO()

		#Resize/modify the image
	    im = im.resize( (1000,1000) )

		#after modifications, save it to the output
	    im.save(output, format='JPEG', quality=100)
	    output.seek(0)

		#change the imagefield value to be the newley modifed image value
	    self.cover_image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.cover_image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

	    super(ProjectName,self).save()
    

    def __str__(self):
        return self.title

    
