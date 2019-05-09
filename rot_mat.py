import numpy as np
from math import sin, cos, pi

def rot_phi(phi):
    phi = phi * pi / 180
    return np.array([
        [1.0, 0.0, 0.0],
        [0.0, cos(phi), sin(phi)],
        [0.0, -sin(phi), cos(phi)]
    ])

def rot_theta(theta):
    theta = theta * pi / 180
    return np.array([
        [cos(theta), 0.0, -sin(theta)],
        [0.0, 1.0, 0.0],
        [sin(theta), 0.0, cos(theta)]
    ])

def rot_si(si):
    si = si * pi / 180
    return np.array([
        [cos(si), sin(si), 0.0],
        [-sin(si), cos(si), 0.0],
        [0.0, 0.0, 1]
    ])

def R(phi, theta, si):
    return np.round(np.matmul(np.matmul(rot_phi(phi), rot_theta(theta)), rot_si(si)), 4)

def deri_R_phi(phi, theta, si):
    phi = phi * pi / 180
    deri_r_array = np.array([
        [0.0, 0.0, 0.0],
        [0.0, -sin(phi), cos(phi)],
        [0.0, -cos(phi), -sin(phi)]
    ])
    return np.round(np.matmul(np.matmul(deri_r_array, rot_theta(theta)), rot_si(si)), 4)

def deri_R_theta(phi, theta, si):
    theta = theta * pi / 180
    deri_r_array = np.array([
        [-sin(theta), 0.0, -cos(theta)],
        [0.0, 0.0, 0.0],
        [cos(theta), 0.0, -sin(theta)]
    ])
    return np.round(np.matmul(np.matmul(deri_r_array, rot_theta(theta)), rot_si(si)), 4)

def deri_R_si(phi, theta, si):
    si = si * pi / 180
    deri_r_array = np.array([
        [-sin(si), cos(si), 0.0],
        [-cos(si), -sin(si), 0.0],
        [0.0, 0.0, 0.0]
    ])
    return np.round(np.matmul(np.matmul(deri_r_array, rot_theta(theta)), rot_si(si)), 4)

if __name__ == '__main__':
    print R(30, 30, 30)
