from django.db import models

class AuxiliarReport(models.Model):
	id_avaya = models.IntegerField()
	name = models.CharField(max_length=255)
	extension =  models.CharField(max_length=255)
	skill = models.CharField(max_length=255)
	date = models.DateField()
	calls_acd = models.IntegerField()
	down_calls = models.IntegerField()
	aht = models.FloatField()
	conversation_time = models.FloatField()
	hold_time = models.FloatField()
	acd_time =  models.FloatField()
	available_time = models.FloatField()
	default_aux = models.FloatField()
	break_aux = models.FloatField()
	floor_walker_aux = models.FloatField()
	qa_feedback = models.FloatField()
	client_trainning_aux = models.FloatField()
	client_feedback_aux = models.FloatField()
	trainning =  models.FloatField()
	coaching_aux = models.FloatField()
	client_system_failure =  models.FloatField()
	system_failure = models.FloatField()
	agent_ring_time =  models.FloatField()
	other_time = models.FloatField()
	assigned_time = models.FloatField()

	def __unicode__(self):
		return self.name


