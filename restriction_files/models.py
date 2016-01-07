from django.db import models

class RestricionFile(models.Model):
    file = models.FileField(upload_to="restricion_files")
