from django.contrib import admin
from mydata.models import PersonalData,AboutMyself,WorkCount,Skills,Experience,Education
# Register your models here.

admin.site.register(PersonalData)
admin.site.register(AboutMyself)
admin.site.register(Skills)
admin.site.register(WorkCount)
admin.site.register(Experience)
admin.site.register(Education)