from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	id_softphone = models.IntegerField()
	id_avaya = models.IntegerField()
	phone = models.CharField(max_length=255)
	user = models.OneToOneField(User)



# Create your models here.
