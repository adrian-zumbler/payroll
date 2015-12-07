from django.db import models

class ScheduleReport(models.Model):
	date = models.DateField()
	name = models.CharField(max_length=255)
	start_time = models.CharField(max_length=255)
	end_time = models.CharField(max_length=255)
	dayly_hours = models.FloatField()
	no_paid_time = models.FloatField()
	paid_time = models.FloatField()
	break_time = models.FloatField()

	def __unicode__(self):
		return self.name
