# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0002_agent_payroll_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='employee_number',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=False,
        ),
    ]
