import numpy
import rospy
from datetime import datetime
import matplotlib.pyplot as plt
from pyquaternion import Quaternion

from geometry_msgs.msg import Vector3
from sensor_msgs.msg import Imu
from std_msgs.msg import Int64
from auv_msgs.msg import AuvState

from kalman_new import *

ERROR_DATA = [[],[],[]]
x, y ,z = 'x', 'y', 'z'


current_data = {
    'old_data': {x:0, y:0, z:0},
    'new_data': {x:0, y:0, z:0},
    'velocity': {x:0, y:0, z:0},
    'previous_data_arrival' : datetime.now()
}

kf = KalmanFilter(F = F_t, H = H_t)

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
    time_sq = ((datetime.now() - current_data['previous_data_arrival']).total_seconds())
    a = Quaternion([0, msg.linear_acceleration.x, msg.linear_acceleration.y, msg.linear_acceleration.z])
    q = Quaternion(msg.orientation.w, msg.orientation.x, msg.orientation.y, msg.orientation.z)
    out_a = q * a / q

    out_a.x = round(out_a.x, 6)
    out_a.y = round(out_a.y, 6)
    out_a.z = round(out_a.z + 10, 6)
    # out_a.z = out_a.z + 10

    current_data['velocity']['x'] = current_data['velocity']['x'] + (time_sq * out_a.x * 100)
    current_data['velocity']['y'] = current_data['velocity']['y'] + (time_sq * out_a.y * 100)
    current_data['velocity']['z'] = current_data['velocity']['z'] + (time_sq * out_a.z * 100)

    current_data['new_data'][x] += (current_data['velocity']['x'] * time_sq)  + (out_a.x * 50 * (time_sq ** 2))
    current_data['new_data'][y] += (current_data['velocity']['y'] * time_sq)  + (out_a.y * 50 * (time_sq ** 2))
    current_data['new_data'][z] += (current_data['velocity']['z'] * time_sq)  + (out_a.z * 50 * (time_sq ** 2))

    current_data['new_data']['x'] = round(current_data['new_data']['x'], 4)
    current_data['new_data']['y'] = round(current_data['new_data']['y'], 4)
    current_data['new_data']['z'] = round(current_data['new_data']['z'], 4)

    pub_msg.acceleration.x = out_a.x
    pub_msg.acceleration.y = out_a.y
    pub_msg.acceleration.z = out_a.z
    pub_msg.velocity.x = current_data['velocity']['x']
    pub_msg.velocity.y = current_data['velocity']['y']
    pub_msg.velocity.z = current_data['velocity']['z']
    pub_msg.position.x = current_data['new_data'][x]
    pub_msg.position.y = current_data['new_data'][y]
    pub_msg.position.z = current_data['new_data'][z]
    pub1.publish(pub_msg)
    current_data['previous_data_arrival'] = datetime.now()

def kalman_estimate(msg, pub1):
    global current_data
    pub_msg = AuvState()
    dt = ((datetime.now() - current_data['previous_data_arrival']).total_seconds())

    a = Quaternion([0, msg.linear_acceleration.x, msg.linear_acceleration.y, msg.linear_acceleration.z])
    q = Quaternion(msg.orientation.w, msg.orientation.x, msg.orientation.y, msg.orientation.z)
    out_a = q * a / q

    out_a.x = round(out_a.x * 100.0, 4)
    out_a.y = round(out_a.y * 100.0, 4)
    out_a.z = round((out_a.z + 10) * 100.0, 4)

    z = np.array([[out_a.x], [out_a.y], [out_a.z]])

    kf.predict(dt = dt)
    kf.update(z= z, dt = dt)

    pub_msg = state_to_rosmsg(kf.x)
    pub1.publish(pub_msg)

    current_data['previous_data_arrival'] = datetime.now()

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
