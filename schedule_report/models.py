from django.db import models

class ScheduleReport(models.Model):
	date = models.DateField()
	name = models.CharField(max_length=255)
	start_time = models.CharField(max_length=255)
	end_time = models.CharField(max_length=255)
	daily_hours = models.FloatField()
	no_paid_time = models.FloatField()
	paid_time = models.FloatField()
	break_time = models.FloatField()
	lunch_time = models.FloatField(null=True)
	absence_time = models.FloatField(null=True)
	green_time = models.FloatField(null=True)
	addtional_time = models.FloatField(null=True)
	gab_time = models.FloatField(null=True)
	vacation_time = models.FloatField(null=True)


	def __unicode__(self):
		return self.name
