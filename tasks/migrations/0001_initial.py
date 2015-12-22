# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activities', '0001_initial'),
        ('agents', '0004_auto_20150809_1224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_to_do', models.DateField()),
                ('start_time', models.CharField(max_length=5, null=True, blank=True)),
                ('end_time', models.CharField(max_length=5, null=True, blank=True)),
                ('comment', models.TextField(null=True, blank=True)),
                ('activity', models.ForeignKey(to='activities.Activity')),
                ('agent', models.ForeignKey(to='agents.Agent')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
