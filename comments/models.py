from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    date = models.DateField()
    text = models.TextField()
    validate =  models.BooleanField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.text

        
# Create your models here.
