from django.db import models
from django.contrib.auth.models import User

class ValidatePayroll(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User)
