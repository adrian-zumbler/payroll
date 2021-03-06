from django.db import models
from django.contrib.auth.models import User
#import local models
from agents.models import Agent
from activities.models import Activity
from files.models import File


#import python utilities
from datetime import date



class Task(models.Model):
    STATUS = (
		('pendiente','Pendiente'),
		('aprobado','Aprobado'),
        ('rechazado','Rechazado'),
	)
    date_to_do = models.DateField()
    start_time = models.CharField(max_length=5,blank=True,null=True)
    end_time = models.CharField(max_length=5,blank=True,null=True)
    comment = models.TextField(blank=True,null=True)
    user = models.ForeignKey(User)
    agent = models.ForeignKey(Agent)
    activity = models.ForeignKey(Activity)
    created = models.DateField(default=date.today().isoformat())
    status = models.CharField(max_length=200,choices=STATUS,default="pendiente")
    document = models.ManyToManyField(File)
    date_to_finish = models.DateField(blank=True,null=True)
