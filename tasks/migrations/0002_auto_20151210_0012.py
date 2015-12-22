# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created',
            field=models.DateField(default=b'2015-12-10'),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default=b'', max_length=200, choices=[(b'pendiente', b'Pendiente'), (b'aprobado', b'Aprobado'), (b'rechazado', b'Rechazado')]),
        ),
    ]
