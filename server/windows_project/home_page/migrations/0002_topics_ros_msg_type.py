# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topics',
            name='ros_msg_type',
            field=models.CharField(default=datetime.datetime(2018, 3, 11, 6, 28, 18, 922329, tzinfo=utc), max_length=15),
            preserve_default=False,
        ),
    ]
