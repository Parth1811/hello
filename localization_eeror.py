import numpy
import rospy
from datetime import datetime
import matplotlib.pyplot as plt

from geometry_msgs.msg import Vector3
from sensor_msgs.msg import Imu
from std_msgs.msg import Int64
from auv_msgs.msg import AuvState

ERROR_DATA = [[],[],[]]
x, y ,z = 'x', 'y', 'z'


current_data = {
    'old_data': {x:0, y:0, z:0},
    'new_data': {x:0, y:0, z:0},
    'previous_data_arrival' : datetime.now()
}

def newupdate_cb(msg):
    global current_data
    current_data['new_data'] = {
        x: msg.position.x,
        y: msg.position.y,
        z: msg.position.z
    }

def oldupdate_cb(msg):
    global current_data
    current_data['old_data'] = {
        x: msg.position.x,
        y: msg.position.y,
        z: msg.position.z
    }
    current_data['previous_data_arrival'] = datetime.now()


def save_data_cb(msg):
    global ERROR_DATA
    plt.plot(ERROR_DATA[0])
    plt.plot(ERROR_DATA[1])
    plt.plot(ERROR_DATA[2])
    plt.savefig('error_'+ str(datetime.now()) + '.png')
    ERROR_DATA = [[],[],[]]

def double_intergrate_acc_cb(msg, pub1):
    global current_data
    pub_msg = AuvState()
    time_sq = ((datetime.now() - current_data['previous_data_arrival']).total_seconds())**2
    current_data['new_data'][x] += msg.linear_acceleration.x * 100 * time_sq
    current_data['new_data'][y] += msg.linear_acceleration.y * 100 * time_sq
    current_data['new_data'][z] += msg.linear_acceleration.z * 100 * time_sq
    pub_msg.position.x = current_data['new_data'][x]
    pub_msg.position.y = current_data['new_data'][y]
    pub_msg.position.z = current_data['new_data'][z]
    pub1.publish(pub_msg)



def pub_error(pub):
    global ERROR_DATA
    rate = rospy.Rate(10)
    while(not rospy.is_shutdown()):
        try:
            msg = Vector3()
            msg.x = current_data['new_data'][x] - current_data['old_data'][x]
            msg.y = current_data['new_data'][y] - current_data['old_data'][y]
            msg.z = current_data['new_data'][z] - current_data['old_data'][z]
            ERROR_DATA[0].append(msg.x)
            ERROR_DATA[1].append(msg.y)
            ERROR_DATA[2].append(msg.z)
            pub.publish(msg)
            rate.sleep()
        except:
            exit()

def subscribe():
    # rospy.Subscriber("/localization_new/pose", AuvState, newupdate_cb)
    pub1 = rospy.Publisher('/localization_new/pose', AuvState, queue_size=10)
    rospy.Subscriber("/imu/data", Imu, double_intergrate_acc_cb, pub1)
    rospy.Subscriber("/localization/pose", AuvState, oldupdate_cb)
    rospy.Subscriber("/save_data", Int64, save_data_cb)
    pub = rospy.Publisher('/error', Vector3, queue_size=10)
    return pub

if __name__ == '__main__':
    rospy.init_node('loc_error')
    pub = subscribe()
    pub_error(pub)
