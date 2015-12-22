# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20151210_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default=b'pendiente', max_length=200, choices=[(b'pendiente', b'Pendiente'), (b'aprobado', b'Aprobado'), (b'rechazado', b'Rechazado')]),
        ),
    ]
