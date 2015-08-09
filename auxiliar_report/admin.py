from django.contrib import admin
from .models import AuxiliarReport

class AuxiliarReportAdmin(admin.ModelAdmin):
	pass

admin.site.register(AuxiliarReport,AuxiliarReportAdmin)	
# Register your models here.
