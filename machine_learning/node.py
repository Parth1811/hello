import random
from matplotlib import pyplot as plt

class points:
    def __init__(self):
        self.x = random.randint(-400,400)
        self.y = random.randint(-400,400)
        self.label = 0 

def fill_data(m,c):
    p_arr = []
    for r in range(10000):
        pt = points()
        if (pt.y >= (m*pt.x +c)):
            pt.label = 1
        if (pt.y < (m*pt.x +c)):
            pt.label = -1
        p_arr.append(pt)
    return p_arr






class node:
    def __init__(self):
        self.inputs = []
        self.weights = []
        self.weights.append(random.randint(-100,100)/100.0)
        self.weights.append(random.randint(-100,100)/100.0)

    def guess(self,inputs):
        sum = 0
        i = 0
        for j in inputs:
            sum += j*self.weights[i]
            i += 1
        guess = sign(sum)
        return guess

    def fit(self,p_arr): 
        for i in range(10000):
            b = [p_arr[i].x,p_arr[i].y]
            guess = self.guess(b)
            error =  p_arr[i].label - guess
            for j in range (2):
                self.weights[j] += error * b[j] * 0.001


def sign (x):
    if (x >= 0):
        return 1
    if (x < 0):
        return -1


p_arr = fill_data(6/7.0,1317/647.0)
n = node()
over_acc = 0
n.fit(p_arr)

for i in range (100):
    p_arr = fill_data(6/7.0,1317/647.0)
    accuracy  = 0
    for i in range (10000):
         #print ("-----------------------------------------------")
        #print (p_arr[i].x)
        #print (p_arr[i].y)
        #print (p_arr[i].label)
        b = [p_arr[i].x,p_arr[i].y]
        if (p_arr[i].label == n.guess(b)):
            accuracy += 1
        #print (n.guess(b))
    #print (accuracy/100.0)
    over_acc += accuracy/100.0

print (over_acc/100.0)

"""
flag = 1
while flag:
    b = []
    b.append(input())
    b.append(input())
    flag = input()
    guess = str(n.guess(b))
    print ("the no is in class : " + guess)
"""
