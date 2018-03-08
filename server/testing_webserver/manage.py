#!/usr/bin/env python
import os
import sys
import rospy

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testing_webserver.settings")
    try:
        rospy.init_node('checker', anonymous=True)
    except:
        pass

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
