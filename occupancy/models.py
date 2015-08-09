from django.db import models

class Occupancy(models.Model):
	date = models.DateField()
	business_line = models.CharField(max_length=255)
	interval_start = models.CharField(max_length=255)
	interval_end = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	id_softphone = models.IntegerField()
	piloto = models.CharField(max_length=255)
	assigned_time = models.FloatField()
	conversation_time = models.FloatField()
	aht = models.FloatField()
	occupancy_percentage = models.FloatField()
	calls_handled = models.IntegerField()

	def __unicode__(self):
		return self.name