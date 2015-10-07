from django.contrib import admin
from .models import Occupancy

class OccupancyAdmin(admin.ModelAdmin):
	list_display = ['name','date','assigned_time',]

admin.site.register(Occupancy,OccupancyAdmin)
