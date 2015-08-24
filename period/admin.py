from django.contrib import admin
from .models import Period
class PeriodAdmin(admin.ModelAdmin):
    pass

admin.site.register(Period, PeriodAdmin)
