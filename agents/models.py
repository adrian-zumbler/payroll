from django.db import models
from django.contrib.auth.models import User

class Agent(models.Model):

	STATUS = (
		('Activo','activo'),
		('Baja','baja'),
	)

	first_name = models.CharField(
		max_length=255,
	)
	last_name = models.CharField(
		max_length=255,
	)
	employee_number = models.IntegerField(
		blank=True,
		null=False
	)
	start_date = models.DateField(
	)
	end_date = models.DateField(
		blank=True,
		null=True
	)
	username_avaya = models.CharField(
		max_length=255,
		blank=True,
		null=True
	)
	id_avaya = models.CharField(
		max_length=4,
		blank=True,
		null=True
	)
	name_avaya = models.CharField(
		max_length=255,
		blank=True,
		null=True
	)
	id_softphone = models.CharField(
		max_length=4,
		blank=True,
		null=True
	)
	min_hours = models.IntegerField(
		blank=True,
		null=True
	)
	max_hours = models.IntegerField(
		blank=True,
		null=True
	)
	phone = models.CharField(max_length=255,
		blank=True,
		null=True
	)
	status = models.CharField(
		max_length=10,
		choices=STATUS,
		default=STATUS[0]
	)
	payroll_number = models.CharField(
		max_length=10,
		blank=True,
		null=True
	)
	user = models.ForeignKey(
		User,
		null=True,
		blank=True
	)

	def __unicode__(self):
		return u'%s %s'	% (self.first_name,self.last_name)

	def fullName(self):
		return u'%s %s'	% (self.first_name,self.last_name)
