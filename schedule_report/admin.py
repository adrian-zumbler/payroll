from django.contrib import admin
from .models import ScheduleReport

class AdminScheduleReport(admin.ModelAdmin):
    list_display = ('name','date',)

admin.site.register(ScheduleReport,AdminScheduleReport)

# Register your models here.
