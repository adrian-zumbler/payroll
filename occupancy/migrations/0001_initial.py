# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Occupancy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('business_line', models.CharField(max_length=255)),
                ('interval_start', models.CharField(max_length=255)),
                ('interval_end', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('id_softphone', models.IntegerField()),
                ('piloto', models.CharField(max_length=255)),
                ('assigned_time', models.FloatField()),
                ('conversation_time', models.FloatField()),
                ('aht', models.FloatField()),
                ('occupancy_percentage', models.FloatField()),
            ],
        ),
    ]
