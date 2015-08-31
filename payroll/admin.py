from django.contrib import admin
from .models import Payroll

class PayrollAdmin(admin.ModelAdmin):
    list_display = ('date',)

admin.site.register(Payroll,PayrollAdmin)
