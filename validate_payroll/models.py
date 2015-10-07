from django.db import models
from django.contrib.auth.models import User

class ValidatePayroll(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return ('%s %s') % (self.date,self.user.username)
