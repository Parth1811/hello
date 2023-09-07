import rospy
import threading
import time
from auv_msgs.msg import DvlData

class Checker:
    def __init__(self, maxtime_):
        self.status_map = {'dvlStatus':False}
        self.numDvl = 0
        self.maxtime = maxtime_
        self.sb = rospy.Subscriber("/dvl/data", DvlData, self.cbDvl)

    def cbDvl(self,data):
        self.numDvl += 1
        if self.numDvl > 10:
            self.status_map['dvlStatus'] = True

    def run(self):
        self.numDvl = 0
        startTime = datetime.now()
        while ((not self.status_map['dvlStatus']) and timeoutFlag):
            currTime = datetime.now()
            timeoutFlag = (currTime - startTime) < self.maxtime
        return self.status_map
