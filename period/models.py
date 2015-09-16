from django.db import models

class Period(models.Model):
    start_date = models.DateField()

    def __unicode__(self):
        return str(self.start_date)
