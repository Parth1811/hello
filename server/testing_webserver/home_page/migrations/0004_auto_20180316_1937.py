# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import home_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0003_auto_20180311_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='matsya_functions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=15)),
                ('function_name', models.CharField(help_text=b'This is the exact name of function as in Matsya.py in auv_state', max_length=25)),
            ],
        ),
        migrations.AlterField(
            model_name='topics',
            name='ros_msg_type',
            field=models.CharField(max_length=15, validators=[home_page.models.validate_even]),
        ),
    ]
