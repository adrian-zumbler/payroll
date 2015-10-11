from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.views.generic import View
from .models import Occupancy
import datetime
import unicodedata

class OccupancyImportView(View):
	template_name = "import.html"

	def get(self,request):
		return render(request,'occupancy/import.html')

	def post(self,request):
		fecha = request.POST.get('date').split('/')
		fecha = '%s-%s-%s' %(fecha[2],fecha[1],fecha[0])
		data = request.FILES.get('file',False)
		path = default_storage.save('tmp/occupancy.txt',ContentFile(data.read()))
		file = default_storage.open(path)
		actual_id = 0
		last_id = 0
		last_name = ""
		sum_assigned_time = 0
		sum_conversation_time = 0
		aux_name = ""
		interval_end = ""
		interval_start = ""
		business_line = ""
		piloto = ""
		aht = 0
		occupancy_percentage = 0
		sum_calls_handled = 0

		flag = False
		for l in file:
			line = l.split('\t')
			actual_id = line[4]
			aux_name = unicodedata.normalize('NFKD',line[3].decode('latin-1')).encode('ASCII','ignore'),
			if actual_id != '':
				if flag == False:
					sum_assigned_time = float(line[6])
					sum_conversation_time = float(line[7])
					try:
						sum_calls_handled = (float(line[7])/float(line[8]))
					except ZeroDivisionError:
						sum_calls_handled = 0
					flag = True
					last_id = actual_id

				if actual_id == last_id:
					sum_assigned_time += float(line[6])
					sum_conversation_time += float(line[7])
					try:
						sum_calls_handled += (float(line[7])/float(line[8]))
					except ZeroDivisionError:
						sum_calls_handled += 0
				else:
					business_line = unicodedata.normalize('NFKD',line[0].decode('latin-1')).encode('ASCII','ignore'),
					interval_start = line[1]
					interval_end = line[2]
					piloto = unicodedata.normalize('NFKD',line[5].decode('latin-1')).encode('ASCII','ignore'),
					aht = 0
					occupancy_percentage = 0
					occupancy = Occupancy.objects.create(
					date = fecha,
					business_line = business_line,
					interval_start = interval_start,
					interval_end = interval_end,
					name = last_name,
					id_softphone = last_id,
					piloto = piloto,
					assigned_time = (sum_assigned_time)/3600,
					conversation_time = (sum_conversation_time)/3600,
					aht = aht,
					occupancy_percentage = occupancy_percentage,
					calls_handled = sum_calls_handled,
					)
					occupancy.save()
					sum_assigned_time = 0
					sum_conversation_time = 0
					flag = False

				last_id = actual_id
				last_name = aux_name

		occupancy = Occupancy.objects.create(
			date = fecha,
			business_line = business_line,
			interval_start = interval_start,
			interval_end = interval_end,
			name = last_name,
			id_softphone = last_id,
			piloto = piloto,
			assigned_time = (sum_assigned_time)/3600,
			conversation_time = (sum_conversation_time)/3600,
			aht = aht,
			occupancy_percentage = occupancy_percentage,
			calls_handled = sum_calls_handled,
		)
		occupancy.save()
		return render(request,'importFiles/import.html',{'success':'Se han cargado los datos con exito'})
