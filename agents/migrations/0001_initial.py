# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('employee_number', models.IntegerField(null=True, blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True, blank=True)),
                ('username_avaya', models.CharField(max_length=255, null=True, blank=True)),
                ('id_avaya', models.CharField(max_length=4, null=True, blank=True)),
                ('name_avaya', models.CharField(max_length=255, null=True, blank=True)),
                ('id_softphone', models.CharField(max_length=4, null=True, blank=True)),
                ('min_hours', models.IntegerField(null=True, blank=True)),
                ('max_hours', models.IntegerField(null=True, blank=True)),
                ('phone', models.CharField(max_length=255, null=True, blank=True)),
                ('status', models.CharField(default='activo', max_length=10, choices=[(b'Activo', b'activo'), (b'Baja', b'baja')])),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
