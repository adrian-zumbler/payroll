from django.db import models



class File(models.Model):
    document = models.FileField(upload_to='restriction_files')
