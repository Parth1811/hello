import numpy as np
from rot_mat import *

from auv_msgs.msg import AuvState

class KalmanFilter(object):
    def __init__(self, F = None, B = None, H = None, Q = None, R = None, P = None, x0 = None):

        if(F is None or H is None):
            raise ValueError("Set proper system dynamics.")

        self.n = 9      #state variables
        self.o = 3      #Control variables
        self.m = 3      #measurement variables

        self.F = F
        self.H = H
        self.B = np.zeros((9,3))

        self.R = np.eye(9,9)
        self.Q = np.eye(3,3)

        self.P = np.eye(9,9)
        self.x = np.zeros((9,1))

    def predict(self, u = 0, dt = 0.001):
        self.x = np.dot(self.F(dt), self.x) #+ np.dot(self.B, u)
        self.P = np.dot(np.dot(self.F(dt), self.P), self.F(dt).T) + self.R
        return self.x

    def update(self, z, dt = 0.001):
        y = z - np.dot(self.H(dt), self.x)
        S = self.Q + np.dot(self.H(dt), np.dot(self.P, self.H(dt).T))
        K = np.dot(np.dot(self.P, self.H(dt).T), np.linalg.inv(S))
        self.x = self.x + np.dot(K, y)
        I = np.eye(9)
        self.P = np.dot(I - np.dot(K, self.H(dt)), self.P) #, (I - np.dot(K, self.H(dt))).T) + np.dot(np.dot(K, self.R), K.T)

def F_t(t):
    t2 = (t**2) / 2.0
    Ft = np.array([
        [1,0,0, t,0,0, t2,0,0],
        [0,1,0, 0,t,0, 0,t2,0],
        [0,0,1, 0,0,t, 0,0,t2],
        [0,0,0, 1,0,0, t,0,0],
        [0,0,0, 0,1,0, 0,t,0],
        [0,0,0, 0,0,1, 0,0,t],
        [0,0,0, 0,0,0, 1,0,0],
        [0,0,0, 0,0,0, 0,1,0],
        [0,0,0, 0,0,0, 0,0,1],
    ])

    return Ft

def H_t(t):
    t2 = (t**2) / 2.0
    Ht = np.array([
        [0,0,0, 0,0,0, 1,0,0],
        [0,0,0, 0,0,0, 0,1,0],
        [0,0,0, 0,0,0, 0,0,1],
    ])
    return Ht

def state_to_rosmsg(x):
    msg = AuvState()
    msg.position.x = float(x[0])
    msg.position.y = float(x[1])
    msg.position.z = float(x[2])
    msg.velocity.x = float(x[3])
    msg.velocity.y = float(x[4])
    msg.velocity.z = float(x[5])
    msg.acceleration.x = float(x[6])
    msg.acceleration.y = float(x[7])
    msg.acceleration.z = float(x[8])

    return msg

def example():
    pass

if __name__ == '__main__':
    example()
