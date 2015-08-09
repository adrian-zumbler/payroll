from django.db import models

class Activity(models.Model):
	name = models.CharField(max_length=255)
	paid = models.BooleanField()


	def __unicode__(self):
		return self.name