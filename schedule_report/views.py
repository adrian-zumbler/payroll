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
		lunch_time = float()
		green_time = float()
		absence_time = float()
		break_time = float()
		start_time = str()
		end_time = str()
		additional_time = float()
		gab_time = float()
		time = str()
		ACTCOUNT = 14
		TIMECOUNT = 13
		start_turn = str()
		end_turn = str()
		immediate = 'Immediate'
		additional_time_label = 'Additional Time'
		general_absence_label = "General Absence"
		vacation_label = "Vacation"
		gab_label = "Shift/Overtime Gap"
		green_time_label = "Green Time"
		lunch_label = "Lunch"




		lunch = 'Lunch'
		break_label = 'Break'
		break_time = float()
		lunchpaid = 0
		for l in file:
			line = l.split('\t')
			for x in line:
				activity = x[:len(x) - ACTCOUNT]
				if activity in ('Break','Lunch','Immediate','Green Time','Shift/Overtime Gap','General Absence',"Additional Time"):
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
					elif activity == additional_time_label:
						additional_time += float(((t2.hour*60) + t2.minute)) - float(((t1.hour*60) + t1.minute))

					else:
						try:
							activityObject = Activity.objects.get(name=activity)
							if activity == lunch_label:
									lunch_time = (float(((t2.hour*60) + t2.minute)) - float(((t1.hour*60) + t1.minute)))
							if activity == break_label:
									break_time+= float(((t2.hour*60) + t2.minute)) - float(((t1.hour*60) + t1.minute))
							if activity == general_absence_label:
									absence_time+= float(((t2.hour*60) + t2.minute)) - float(((t1.hour*60) + t1.minute))
							if activity == green_time_label:
									green_time+= float(((t2.hour*60) + t2.minute)) - float(((t1.hour*60) + t1.minute))
							if activity == gab_label:
									gab_time+= float(((t2.hour*60) + t2.minute)) - float(((t1.hour*60) + t1.minute))

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
				daily_hours = float((stayTime - lunch_time -additional_time)/60),
				no_paid_time = 0,
				paid_time = float((stayTime - green_time - absence_time - gab_time - lunch_time)/60),
				break_time = float(break_time/60),
				addtional_time = float(additional_time/60),
				absence_time = float(absence_time/60),
				lunch_time = float(lunch_time/60),
				green_time = float(green_time/60),
				gab_time = float(gab_time/60),

				)
			schedule.save()
			NoPaidTime = 0
			paidTime = 0
			lunchpaid = 0
			stayTime = 0
			start_turn = ''
			end_turn = ''
			break_time = 0
			gab_time = 0
			absence_time = 0
			lunch_time = 0
			green_time = 0
			additional_time = 0
		return render(request,'importFiles/import.html',{'success' : 'Se cargaron los datos con exito'})
