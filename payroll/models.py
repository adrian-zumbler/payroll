from django.db import models
from agents.models import Agent

class Payroll(models.Model):
    date = models.DateField()
    schedule_time =  models.FloatField()
    adjusted = models.FloatField()
    softphone =  models.FloatField()
    avaya = models.FloatField()
    aux = models.FloatField()
    paid_total = models.FloatField()
    status = models.CharField(max_length=2)
    agent = models.ForeignKey(Agent)
