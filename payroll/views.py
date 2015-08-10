from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.core import serializers
from agents.models import Agent
from occupancy.models import Occupancy
from auxiliar_report.models import AuxiliarReport
from schedule_report.models import ScheduleReport
import json
from django.http import HttpResponse
from django.template.response import TemplateResponse


class PayrollView(View):

	def get(self,request):
		
		payroll = []
		CARTERA_PAID = 'Cartera Desborde'
		agents = Agent.objects.all()
		for agent in agents:
			data = {}
			data['schedule'] = 0
			data['paid_time'] = 0
			data['time_off'] = 0
			data['time_avaya'] = 0
			data['aux_paid'] = 0
			data['time_softphone'] = 0
			data['name'] = '%s %s' % (agent.first_name,agent.last_name)
			if agent.id_softphone != "":
				occupancy = Occupancy.objects.all().filter(id_softphone = agent.id_softphone).filter(date='2015-08-03')
				for oc in occupancy:
					data['time_softphone'] = oc.assigned_time
			if agent.name_avaya != "":
				try:
					schedule =  ScheduleReport.objects.all().filter(name = agent.name_avaya).filter(date='2015-08-03')
					for sh in schedule:
						data['schedule'] = sh.dayly_hours
						data['time_off'] = sh.no_paid_time  
						data['paid_time'] = sh.paid_time	
				except Exception:
					pass	
			if agent.id_avaya != "":
				try:
					avaya = AuxiliarReport.objects.all().filter(id_avaya = agent.id_avaya).filter(date='2015-08-03')
					for a in avaya:
						if a.skill == CARTERA_PAID:
							data['time_avaya'] += a.assigned_time/3600
						else:
							data['aux_paid'] += (a.assigned_time - a.available_time)/3600

				except Exception:
					pass		

			data['paid_total'] = (data['time_softphone'] + data['time_avaya'] + data['aux_paid']) 
			data['paid_total'] = data['paid_total'] if data['paid_total'] > 0 else 0
			payroll.append(data)
		return HttpResponse(json.dumps(payroll))


class PayrollDayView(View):

	def get(self,request):
		return render(request,'payroll/payday.html')

