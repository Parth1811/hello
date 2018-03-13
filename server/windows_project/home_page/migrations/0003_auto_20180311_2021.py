# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0002_topics_ros_msg_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topics',
            name='ros_msg_type',
            field=models.CharField(max_length=15, choices=[(b'DVL', b'DvlData'), (b'IMU', b'IMUDATA')]),
        ),
    ]
