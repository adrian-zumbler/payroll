from django.shortcuts import render, redirect
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
import pdb
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Payroll
import django_excel as excel
import pyexcel.ext.xls
from datetime import datetime, timedelta




class PayrollView(View):

	def post(self,request):
		payroll = []
		day = request.POST.get('day')
		print request.POST
		CARTERA_PAID = 'Cartera Desborde'
		if request.user.is_staff:
			agents = Agent.objects.all().filter(status='Activo')
		else:
			agents = Agent.objects.all().filter(user__username=request.user.username).filter(status='Activo')
		for agent in agents:
			data = {}
			data['schedule'] = 0
			data['paid_time'] = 0
			data['time_off'] = 0
			data['time_avaya'] = 0
			data['aux_paid'] = 0
			data['time_softphone'] = 0
			data['name'] = '%s %s' % (agent.first_name,agent.last_name)
			data['payroll_number'] =  agent.payroll_number
			if agent.id_softphone != "":
				occupancy = Occupancy.objects.all().filter(id_softphone = agent.id_softphone).filter(date=day)


				for oc in occupancy:
					data['time_softphone'] = oc.assigned_time
			if agent.name_avaya != "":
				try:
					schedule =  ScheduleReport.objects.all().filter(name = agent.name_avaya).filter(date=day)
					for sh in schedule:
						data['schedule'] = sh.dayly_hours
						data['time_off'] = sh.no_paid_time
						data['paid_time'] = sh.paid_time
				except Exception:
					pass
			if agent.id_avaya != "":
				try:
					avaya = AuxiliarReport.objects.all().filter(id_avaya = agent.id_avaya).filter(date=day)
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

		#payroll = Task.objects.all()
		#data_send = serializers.serialize("json", payroll)

		return HttpResponse(json.dumps(payroll), content_type='application/json')

class PayRollSaveAjaxView(View):

	def post(self,request):
		date = request.POST.get('day')
		payroll_number = request.POST.get('payroll_number')
		name = request.POST.get('name')
		schedule = request.POST.get('schedule')
		adjusted = request.POST.get('adjusted')
		softphone = request.POST.get('softphone')
		avaya = request.POST.get('avaya')
		aux = request.POST.get('aux')
		paid_total = request.POST.get('paid_total')
		status = request.POST.get('status')

		agent = Agent.objects.get(payroll_number = payroll_number)

		payroll = Payroll.objects.create(
			date = date,
		    schedule_time =  schedule,
		    adjusted = adjusted,
		    softphone =  softphone,
		    avaya = avaya,
		    aux = aux,
		    paid_total = paid_total,
		    status = status,
			agent = agent
		)
		payroll.save()
		print 'OK'

		return HttpResponse({'data':'Hola'})


class PayrollDayView(View):

	def get(self, request):
		if request.user.is_authenticated():
			return render(request,'payroll/payday.html')
		else:
			return redirect('%s?next=%s' % (settings.LOGIN_URL,request.path))


class PayrollWeekView(View):

	def get(self, request):
		if request.user.is_authenticated():
			return render(request, 'payroll/payweek.html')
		else:
			return redirect('%s?next=%s' % (settings.LOGIN_URL,request.path))

class PayrollWeekAjaxView(View):

	def post(self,request):
		payroll_week = []
		start_date = request.POST.get('day')
		auxdate = datetime.strptime(start_date,'%Y-%m-%d')
		end_date = auxdate + timedelta(days=7)
		end_date = end_date.strftime('%Y-%m-%d')
		agents = Agent.objects.filter(user__id = request.user.id)
		payrolls = Payroll.objects.all().filter(date__gte=start_date,date__lte=end_date)
		payrolls = payrolls.filter(agent__user__username = request.user.username)
		for agent in agents:
			agent_week = []
			payrolls = Payroll.objects.all().filter(agent__id = agent.id)
			payrolls = payrolls.filter(date__gte=start_date,date__lte=end_date)
			for payroll in payrolls:
				agent = []
				data = {}
				data['payroll_number'] = payroll.agent.payroll_number
				data['name'] = payroll.agent.first_name
				data['date'] = str(payroll.date)
				data['paid_total'] = payroll.paid_total
				data['status'] = payroll.status
				
				agent_week.append(data)
			payroll_week.append(agent_week)


		return HttpResponse(json.dumps(payroll_week))

class ExportView(View):

	def get(self,request):
		payroll = Payroll.objects.all()
		column_names = ['id']
		payroll = {}
		payroll['id'] = 1
		return excel.make_response_from_query_sets(payroll,column_names,'xls')
