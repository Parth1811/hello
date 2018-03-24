# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import home_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0004_auto_20180316_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matsya_functions',
            name='function_name',
            field=models.CharField(help_text=b'This is the exact name of function as in Matsya.py in auv_state', max_length=25, validators=[home_page.models.validate_matsya_function]),
        ),
    ]
