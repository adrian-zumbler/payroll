from django.db import models

class RestricionFile(models.Model):
    file = models.FileField(upload_to="restriction_files")
