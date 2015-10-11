from django.shortcuts import render
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.core.files.base import ContentFile
from .models import Agent
from django.views.generic import View
import unicodedata
import json
from auxiliar_report.models import AuxiliarReport
from occupancy.models import Occupancy
from payroll.models import Payroll

def export(request):
	if request.method == 'POST':
		data = request.FILES.get('file',False)
		path = default_storage.save('tmp/archivo.txt',ContentFile(data.read()))
		file = default_storage.open(path)
		x = 0
		for l in file:
			line = l.split('\t')
			if line[0] != "":
				agent = Agent.objects.create(
					first_name=unicodedata.normalize('NFKD',line[0].decode('latin-1')).encode('ASCII','ignore'),
					last_name= unicodedata.normalize('NFKD',line[1].decode('latin-1')).encode('ASCII','ignore'),
					employee_number=line[2],
					start_date= line[3],
					min_hours= line[4],
					max_hours= line[5],
					phone=line[6],
					id_softphone = line[7],
					id_avaya = line[8],
					username_avaya = line[11],
					payroll_number = line[10],
					name_avaya = unicodedata.normalize('NFKD',line[9].decode('latin-1')).encode('ASCII','ignore'),
				)
				agent.save()
				x = x + 1

		return render(request,'importFiles/import.html',{'success': "Se han agregado %s registros" %(x)})

	return render(request,'agents/export.html')

class AgentStatisticsView(View):

	def get(self,request):
		agents = Agent.objects.filter(status="Activo")
		statistics = []
		for agent in agents:
			data = {}
			data['name'] = ('%s %s') % (agent.first_name,agent.last_name)
			data['calls'] = 0
			data['time_conversation'] = 0
			data['aht'] = 0
			data['paid_time'] = 0
			data['operation_work_hours'] = 0
			data['OCC'] = 0
			aux_avaya = AuxiliarReport.objects.all().filter(id_avaya = agent.id_avaya).filter(date__gte='2015-10-05',date__lte='2015-10-11')
			for aux in aux_avaya:
				data['calls'] += aux.calls_acd
				data['time_conversation'] += aux.conversation_time/3600
				if aux.skill == 'Cartera Desborde':
					data['operation_work_hours'] += (aux.conversation_time + aux.available_time)/3600


			aux_occ = Occupancy.objects.all().filter(id_softphone = agent.id_softphone).filter(date__gte='2015-10-05',date__lte='2015-10-11')
			for occ in aux_occ:
				data['calls'] += occ.calls_handled
				data['time_conversation'] += occ.conversation_time
				data['operation_work_hours'] += occ.assigned_time

			payrolls = Payroll.objects.all().filter(agent__payroll_number=agent.payroll_number).filter(date__gte='2015-10-05',date__lte='2015-10-11')
			for payroll in payrolls:
				data['paid_time'] += payroll.paid_total


			try:
				data['aht'] = (data['time_conversation']*60)/data['calls']
			except ZeroDivisionError:
				data['aht'] = 0

			try:
				data['OCC'] = data['time_conversation']/data['operation_work_hours']
			except ZeroDivisionError:
				data['OCC'] = 0

			statistics.append(data)

		return HttpResponse(json.dumps(statistics))
