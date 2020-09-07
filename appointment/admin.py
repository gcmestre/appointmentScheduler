from django.contrib import admin
from .models import Appointment, Client, Employee, AppointmentType

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'

admin.site.register(Appointment)
admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(AppointmentType)
