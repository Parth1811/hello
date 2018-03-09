#!/usr/bin/env python
import threading
import os
import rospy
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testing_webserver.settings")
    try:
        rospy.init_node('checker', anonymous=True)
        print("starting")
        threading.Thread(target = rospy.spin).start()
        print("starting 2")
    except:
        pass

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
