import rospy
import threading
import time
from multiprocessing import Process
from auv_msgs.msg import DvlData

class Checker:
    status_map = {'dvlStatus':False}
    numDvl = 0

    def stop_clock(self):
        #time.sleep(10)
        for i in range(10):
            time.sleep(1)
            print('====================')
            print(i)
            print('====================')
        rospy.signal_shutdown(True)


    def cbDvl(self,data):
        self.numDvl += 1
        if self.numDvl > 10:
            self.status_map['dvlStatus'] = True

    def run(self):
        threading.Thread(target = self.stop_clock).start()
        rospy.Subscriber("/dvl/data", DvlData, self.cbDvl)
        rospy.spin()
        return self.status_map

if __name__ == '__main__':
    rospy.init_node('checker', anonymous=True)
    ch = Checker()
    threading.Thread(target = ch.run).start()
