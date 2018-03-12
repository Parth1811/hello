import rospy
import threading
from multiprocessing import Process
import time
import datetime as dt
from std_msgs.msg import Float64
from sensor_msgs.msg import Imu
from auv_msgs.msg import DvlData
from auv_msgs.msg import ElecAtmegaStatus


class Checker:
    def __init__(self, title_, topic_name_,ros_msg_type_ ,timeout_ = 10,threshold_ =10):
        self.num = 0
        self.title = title_
        self.topic_name = topic_name_
        self.msg_type = ros_msg_type_
        self.timeout = timeout_
        self.threshold = threshold_
        self.timeoutFlag = True
        self.mapkey = str(self.title)+"Status"
        self.status_map = {self.mapkey:False}
        self.sb = rospy.Subscriber(self.topic_name,self.ros_msg(self.msg_type) ,self.cb)

    def cb(self,data):
        self.num += 1
        if self.num > 10:
            self.status_map[self.mapkey] = True

    def run(self):
        self.num = 0
        startTime = dt.datetime.now()
        T_ros_spin = Process(target=rospy.spin)
        T_ros_spin.start()
        while ((not self.status_map[self.mapkey]) and self.timeoutFlag):
            currTime = dt.datetime.now()
            self.timeoutFlag = (currTime - startTime).seconds < self.timeout
        T_ros_spin.terminate()
        return self.status_map[self.mapkey]

    def ros_msg(self,msg_type):
        #getattr('DvlData')
        if msg_type== 'DvlData':
            return DvlData
