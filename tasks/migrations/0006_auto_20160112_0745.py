# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
        ('tasks', '0005_auto_20160107_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='document',
            field=models.ManyToManyField(to='files.File'),
        ),
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateField(default=b'2016-01-12'),
        ),
    ]
