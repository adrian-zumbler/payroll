from django.contrib import admin
from .models import ValidatePayroll


class validatePayrollAdmmin(admin.ModelAdmin):
    pass

admin.site.register(ValidatePayroll,validatePayrollAdmmin)
