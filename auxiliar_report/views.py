from django.shortcuts import render
from django.views.generic import View
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import AuxiliarReport
import unicodedata
# -*- coding: utf-8 -*-

class AuxiliarReportImportView(View):

	def get(self,request):
		return render(request,'auxiliarReport/import.html')

	def post(self,request):
		data = request.FILES.get('archivo',False)
		path = default_storage.save('tmp/auxiliar_report.txt',ContentFile(data.read()))
		file = default_storage.open(path)
		for l in file:
			line = l.split('\t')
			auxiliarReport = AuxiliarReport.objects.create(
				id_avaya = line[0],
				name = unicodedata.normalize('NFKD',line[1].decode('latin-1')).encode('ASCII','ignore'),
				extension = line[2],
				skill = line[3],
				date = line[4],
				calls_acd = line[5],
				down_calls = line[6],
				aht = line[7],
				conversation_time = line[8],
				hold_time = line[9],
				acd_time = line[10],
				available_time = line[11],
				default_aux  = line[12],
				break_aux = line[13],
				floor_walker_aux = line[14],
				qa_feedback = line[15],
				client_trainning_aux = line[16],
				client_feedback_aux = line[17],
				trainning = line[18],
				coaching_aux = line[19],
				client_system_failure = line[20],
				system_failure = line[21],
				agent_ring_time = line[22],
				other_time = line[23],
				assigned_time = line[24]
				)
			auxiliarReport.save()
		return render(request,'auxiliarReport/import.html',{'sucess':'Los dato se guardaron con exito'})



