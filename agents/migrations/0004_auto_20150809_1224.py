# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0003_auto_20150727_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='status',
            field=models.CharField(default=(b'Activo', b'activo'), max_length=10, choices=[(b'Activo', b'activo'), (b'Baja', b'baja')]),
        ),
    ]
