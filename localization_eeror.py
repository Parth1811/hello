import numpy
import rospy

from auv_msgs.msg import AuvState
from geometry_msgs.msg import Vector3

current_data = {
    'old_data': {'x':0, 'y':0, 'z':0},
    'new_data': {'x':0, 'y':0, 'z':0}
}

def newupdate_cb(msg):
    global current_data
    current_data['new_data'] = {
        'x': msg.position.x,
        'y': msg.position.y,
        'z': msg.position.z
    }

def oldupdate_cb(msg):
    global current_data
    current_data['old_data'] = {
        'x': msg.position.x,
        'y': msg.position.y,
        'z': msg.position.z
    }

def pub_error(pub):
    rate = rospy.Rate(10)
    while(True):
        try:
            msg = Vector3()
            msg.x = current_data['new_data']['x'] - current_data['old_data']['x']
            msg.y = current_data['new_data']['y'] - current_data['old_data']['y']
            msg.z = current_data['new_data']['z'] - current_data['old_data']['z']
            pub.publish(msg)
            rate.sleep()
        except:
            exit()

def subscribe():
    rospy.Subscriber("/localization_new/pose", AuvState, newupdate_cb)
    rospy.Subscriber("/localization/pose", AuvState, oldupdate_cb)
    pub = rospy.Publisher('/error', Vector3, queue_size=10)
    return pub

if __name__ == '__main__':
    rospy.init_node('loc_error')
    pub = subscribe()
    pub_error(pub)
