# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0004_auto_20150809_1224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('padi_total', models.FloatField()),
                ('status', models.CharField(max_length=2)),
                ('agent', models.ForeignKey(to='agents.Agent')),
            ],
        ),
    ]
