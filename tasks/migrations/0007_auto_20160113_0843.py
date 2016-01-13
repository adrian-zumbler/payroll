# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20160112_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date_to_finish',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateField(default=b'2016-01-13'),
        ),
    ]
