from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.db import models

import std_msgs.msg as std
import sensor_msgs.msg as sensor
import geometry_msgs.msg as geom
from auv_state import matsya

import auv_msgs.msg as auv


def validate_even(value):
    type_list = [std,sensor,geom,auv]
    flag = True
    for libtype in type_list:
        try:
            getattr(libtype , value)
            flag = False
        except AttributeError:
            pass
    if flag:
        raise ValidationError(
                        _('%(value)s is not an valid ros msg type'),
            params={'value': value},
        )

def validate_matsya_function(func_name):
    try:
        getattr(matsya.Matsya ,func_name)
    except AttributeError:
        raise ValidationError(
                _('%(func_name)s is not an valid function in auv_state/Matsya.py'),
            params={'func_name': func_name},
        )


class topics(models.Model):
    title = models.CharField(max_length=15)
    topic_name = models.CharField(max_length=25)
    MSG_TYPE_CHOICES =  (('DVL', "DvlData"),('IMU', "IMUDATA"))
    ros_msg_type = models.CharField(max_length=15 ,validators=[validate_even])
    max_post_required = models.IntegerField()
    timeout = models.IntegerField()

    def __str__(self):
        return self.title

class matsya_functions(models.Model):
    title = models.CharField(max_length=15)
    help_msg ='This is the exact name of function as in Matsya.py in auv_state'
    function_name = models.CharField(max_length=25, help_text=\
        help_msg, validators = [validate_matsya_function])

    def __str__(self):
        return self.title



