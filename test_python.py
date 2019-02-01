import rospy
from datetime import datetime


from auv_msgs.msg import DvlData

def call_back(msg, arg):
    arg["dvl_pos"]["x"] =  msg.position.x
    arg["dvl_pos"]["y"] =  msg.position.y
    arg["dvl_pos"]["z"] =  msg.position.z
    dt = (datetime.now() - arg["last_msg_time"]).total_seconds()
    arg["pos"]["x"] += msg.velocity.x * dt
    arg["pos"]["y"] += msg.velocity.y * dt
    arg["pos"]["z"] += msg.velocity.z * dt
    arg["error"]["x"] = (arg["pos"]["x"] - arg["dvl_pos"]["x"]) / arg["dvl_pos"]["x"] * 100
    arg["error"]["y"] = (arg["pos"]["y"] - arg["dvl_pos"]["y"]) / arg["dvl_pos"]["y"] * 100
    arg["error"]["z"] = (arg["pos"]["z"] - arg["dvl_pos"]["z"]) / arg["dvl_pos"]["z"] * 100
    print arg["pos"]
    print arg["dvl_pos"]
    print arg["error"]
    print "--------------------------------------"

arg= {
"last_msg_time" : datetime.now(),
"pos" : {"x": 482.05500000000796, "y": -68.7950000000128, "z": -68.7950000000128},
"error": {"x": 0, "y": 0, "z":0},
"dvl_pos" : {"x": 0, "y": 0, "z":0},
}
rospy.init_node('testing')
rospy.Subscriber("/dvl/data", DvlData, call_back, arg)


rospy.spin()
