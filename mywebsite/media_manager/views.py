from django.contrib import messages
from django.http import request
from django.http.response import FileResponse
from django.shortcuts import redirect, render
from PIL import Image
import os,os.path
from mywebsite.settings import MEDIA_URL,BASE_DIR
from mydata.models import PersonalData
from project.models import ProjectName
import re
# Create your views here.

def media_list(request):

    template_name = 'dashboard/pages/media_management/media_mngt/media_managemet.html'
    profile_imgs = []
    project_imgs = []
    profile_img_path = "media/profile_pic/"
    project_img_path = "media/project_pic/"
    valid_images = ['jpg','gif','png','tga']
    for file in os.listdir(profile_img_path):
        src = os.path.join('profile_pic',file)
        name = file.split('.')[0]
        active_img = True if PersonalData.objects.first().image.url.split('.')[0].split('/')[-1] == name else False
        profile_imgs.append({'src':src,'name':name,'active':active_img})
    project = ProjectName.objects.all()
    active_project_imgs = []
    for proj in project:
        active_project_imgs.append(proj.cover_image.url.split('.')[0].split('/')[-1])
    for file in os.listdir(project_img_path):
        src = os.path.join('project_pic',file)
        name = file.split('.')[0]
        active_img = True if name in active_project_imgs else False
        project_imgs.append({'src':src,'name':name,'active':active_img})
    context = {
        'profile_img':profile_imgs,
        'project_img':project_imgs
    }
    return render(request,template_name,context)

def delete_media(request,img_id):

    template_name = 'dashboard/pages/media_management/media_mngt/delete_media.html'
    image_src = os.path.join(MEDIA_URL,img_id)
    context = {
        'image':image_src
    }
    return render(request,template_name,context)

def delete_media_confirm(request):
    
    #file_dir = img_path.split('/','\\')
    if request.method == 'POST':
        image_path = str(request.POST['image'].replace('/','\\'))
        try:
            file_path = BASE_DIR + image_path
            os.remove(file_path)
            messages.success(request,'Your Media is deleted successfully')
        except Exception as e:
            raise e
    return redirect('media_list')

def download_media(request,img_id):
    
    img = BASE_DIR + MEDIA_URL + img_id
    img = img.replace('\\','/')

    d_f = FileResponse(open(img,'rb'))

    return d_f