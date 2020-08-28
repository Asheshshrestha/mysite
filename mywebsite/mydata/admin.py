from django.contrib import admin
from mydata.models import PersonalData,AboutMyself,WorkCount,Skills
# Register your models here.

admin.site.register(PersonalData)
admin.site.register(AboutMyself)
admin.site.register(Skills)
admin.site.register(WorkCount)
