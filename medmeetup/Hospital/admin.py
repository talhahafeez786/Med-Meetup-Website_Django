from django.contrib import admin
from .models import (Slider, Service, Item, Doctor, Gallery, Faq, Expertize)

# Register your models here.

admin.site.register(Slider)
admin.site.register(Service)
admin.site.register(Item)
# admin.site.register(Doctor)
admin.site.register(Doctor)
admin.site.register(Gallery)
admin.site.register(Faq)
admin.site.register(Expertize)

