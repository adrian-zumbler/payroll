from django.db import models

class Period(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    def __unicode__(self):
        return '%s - %s' % (self.start_date,self.end_date)
