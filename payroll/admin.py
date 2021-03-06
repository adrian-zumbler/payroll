from django.contrib import admin
from .models import Payroll
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.admin import DateFieldListFilter
from daterange_filter.filter import DateRangeFilter

class PayrollResource(resources.ModelResource):
    class Meta:
        model = Payroll
        fields = ('id','date','agent__payroll_number','agent__first_name','agent__last_name','schedule_time','status','paid_total','adjusted','agent__user__first_name','agent__user__last_name','agent__start_date')



class PayrollAdmin(ImportExportModelAdmin):
    list_display = ['date', 'getAgentFullName','status','paid_total','getSupervisorFullName']
    list_filter = (
        ('date', DateRangeFilter),
    )
    resource_class = PayrollResource

    def getAgentFullName(self,obj):
        return '%s %s' % (obj.agent.first_name, obj.agent.last_name)

    def getSupervisorFullName(self,obj):
        return '%s %s' % (obj.agent.user.first_name, obj.agent.user.last_name)


admin.site.register(Payroll,PayrollAdmin)
