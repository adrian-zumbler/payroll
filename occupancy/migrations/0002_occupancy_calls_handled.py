# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('occupancy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='occupancy',
            name='calls_handled',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
