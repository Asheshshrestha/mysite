from django.contrib import admin
from mydata.models import (PersonalData,
                            AboutMyself,
                            WorkCount,
                            Skills,
                            Experience,
                            Education,
                            OfferToClient,
                            Offers,
                            TestimonialMessage,
                            Testimonials)
# Register your models here.

admin.site.register(PersonalData)
admin.site.register(AboutMyself)
admin.site.register(Skills)
admin.site.register(WorkCount)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Offers)
admin.site.register(OfferToClient)
admin.site.register(Testimonials)
admin.site.register(TestimonialMessage)