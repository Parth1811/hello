import numpy as np
from rot_mat import *
from auv_msgs.msg import EKFState, ControlData

def calc_postion(current_pos, vel, acc, orientation, alpha, dt):
    next_pos = current_pos + vel*dt + (dt**2)/2.0*(W1)



def F(intial_state, control_data):
    next_state = EKFState()
    next_state.position.x =
