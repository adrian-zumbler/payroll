from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import Agent
import unicodedata


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
