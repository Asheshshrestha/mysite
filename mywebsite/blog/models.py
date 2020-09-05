from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class BlogModel(models.Model):

    category_choose = (('technology','technology'),('lifestyle','lifestyle'),('fashion','fashion'),('art','art'),('food','food'),('architecture','architecture'),('adventure','adventure'))
    title = models.CharField(max_length=200,null= True)
    cover_image = models.ImageField(upload_to='blog_cover/',null=True)
    summary = models.CharField(max_length=500,null=True)
    content = RichTextUploadingField()
    category = models.CharField(max_length=20,choices=category_choose,null=True)
    pub_date = models.DateField(auto_now_add=True)
    view_count = models.IntegerField(null=True,default=0)

    def save(self):
    
		#Opening the uploaded image
	    im = Image.open(self.cover_image)

	    output = BytesIO()

		#Resize/modify the image
	    im = im.resize( (555,280) )

		#after modifications, save it to the output
	    im.save(output, format='JPEG', quality=100)
	    output.seek(0)

		#change the imagefield value to be the newley modifed image value
	    self.cover_image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.cover_image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

	    super(BlogModel,self).save()

    def __str__(self):
        return self.title
