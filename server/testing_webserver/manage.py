#!/usr/bin/env python
import os
import sys
import rospy
import threading

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testing_webserver.settings")
    try:
        rospy.init_node('server',anonymous = True,disable_signals = True)
    except:
        print("ERROR:     Unable to register node, try runing roscore") 

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
