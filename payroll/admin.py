from django.contrib import admin
from .models import Payroll

class PayrollAdmin(admin.ModelAdmin):
    list_display = ['date', 'getAgentFullName']

    def getAgentFullName(self,obj):
        return '%s %s' % (obj.agent.first_name, obj.agent.last_name)

admin.site.register(Payroll,PayrollAdmin)
