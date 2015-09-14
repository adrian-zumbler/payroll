from django.contrib import admin
from .models import Payroll
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class PayrollResource(resources.ModelResource):
    class Meta:
        model = Payroll
        fields = ('id','date','paid_total','agent__first_name')


class PayrollAdmin(ImportExportModelAdmin):
    list_display = ['date', 'getAgentFullName',]
    resource_class = PayrollResource

    def getAgentFullName(self,obj):
        return '%s %s' % (obj.agent.first_name, obj.agent.last_name)



admin.site.register(Payroll,PayrollAdmin)
