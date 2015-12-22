from django.shortcuts import render
from django.views.generic import View
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from activities.models import Activity
from .models import ScheduleReport
import datetime
import unicodedata

class ScheduleReportImportView(View):

	def get(self,request):
		return render(request,'sheduleReport/import.html')

	def post(self,request):
		fecha = request.POST.get('date').split('/')
		fecha = '%s-%s-%s' %(fecha[2],fecha[1],fecha[0])
		data = request.FILES.get('file',False)
		path = default_storage.save('tmp/schedule_export.txt',ContentFile(data.read()))
		file = default_storage.open(path)
		activity = str()
		start = str()
		end = str()
		NoPaidTime = float()
		stayTime =  float()
		paid_time = float()
		start_time = str()
		end_time = str()
		time = str()
		ACTCOUNT = 14
		TIMECOUNT = 13
		start_turn = str()
		end_turn = str()
		immediate = 'Immediate'
		lunch = 'Lunch'
		break_label = 'Break'
		break_time = float()
		lunchpaid = 0
		for l in file:
			line = l.split('\t')
			for x in line:

				activity = x[:len(x) - ACTCOUNT]
				if activity in ('Break','Lunch','Immediate','Green Time','Shift/Overtime Gap','General Absence'):
					time = x[len(x) - TIMECOUNT:]
					end = time[len(time)-5:]
					start = time[:len(time)-8]
					start_time = start.split(':')
					end_time = end.split(':')
					t1 = datetime.time(int(start_time[0]),int(start_time[1]),0)
					t2 = datetime.time(int(end_time[0]),int(end_time[1]),0)
					if activity == immediate:
						stayTime = float(((t2.hour*60) + t2.minute)) - float(((t1.hour*60) + t1.minute))
						start_turn = start
						end_turn = end
						paid_time = stayTime
					else:
						try:
							activityObject = Activity.objects.get(name=activity)
							if activity == lunch:
									lunchpaid = (float(((t2.hour*60) + t2.minute)) - float(((t1.hour*60) + t1.minute)))
									stayTime = stayTime - lunchpaid
							if activity == break_label:
									break_time+= float(((t2.hour*60) + t2.minute)) - float(((t1.hour*60) + t1.minute))
							if activityObject.paid == False:
								NoPaidTime += float(((t2.hour*60) + t2.minute)) - float(((t1.hour*60) + t1.minute))
						except:
							pass
				if x == 'Off':
					paid_time = 0
					stayTime = 0
					start_turn = ''
					end_turn = ''
					break_time = 0

			schedule = ScheduleReport.objects.create(
				date = fecha,
				name = unicodedata.normalize('NFKD',line[0].decode('latin-1')).encode('ASCII','ignore'),
				start_time = start_turn,
				end_time = end_turn,
				dayly_hours = float(stayTime/60),
				no_paid_time = float(NoPaidTime/60),
				paid_time = float((((paid_time - break_time ) - NoPaidTime)-lunchpaid)/60),
				break_time = float(break_time/60)
				)
			schedule.save()
			NoPaidTime = 0
			paidTime = 0
			lunchpaid = 0
			stayTime = 0
			start_turn = ''
			end_turn = ''
			break_time = 0
		return render(request,'importFiles/import.html',{'success' : 'Se cargaron los datos con exito'})
