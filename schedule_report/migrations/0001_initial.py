# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=255)),
                ('start_time', models.CharField(max_length=255)),
                ('end_time', models.CharField(max_length=255)),
                ('dayly_hours', models.FloatField()),
                ('no_paid_time', models.FloatField()),
                ('paid_time', models.FloatField()),
            ],
        ),
    ]
