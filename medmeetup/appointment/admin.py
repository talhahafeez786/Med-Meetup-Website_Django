from django.contrib import admin
from  appointment.models import Appointment
# Register your models here.

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone', 'doctor', 'date','time']
    date_hierarchy = ('date')
    list_filter = ['date','doctor',]
    list_per_page = 20
    search_fields = ['doctor','name',]
