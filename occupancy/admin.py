from django.contrib import admin
from .models import Occupancy

class OccupancyAdmin(admin.ModelAdmin):
	pass

admin.site.register(Occupancy,OccupancyAdmin)	