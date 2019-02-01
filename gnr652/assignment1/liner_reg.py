 #! /usr/bin/python
import numpy as np


data_filepath = 'data/data.csv'
num_of_iter = 500000
alpha = 0.005

# data = open(data_filepath, 'w').readlines()
data = np.genfromtxt(data_filepath, delimiter=',')
data = np.array(data[1:])
data_array = np.ones((data.shape[0], data.shape[1]+1))
data_array[:,1:] = data
data = data_array

x_train = data[:data.shape[0]*0.8,:-1]
y_train = data[:data.shape[0]*0.8,-1]
x_test = data[data.shape[0]*0.8:,:-1]
y_test = data[data.shape[0]*0.8:,-1]


weights = np.random.rand(18)

# for i in range (num_of_iter):
#     diff = x_train.dot(weights) - y_train
#     func_J = 0.5* (((diff)**2).sum())
#     avg_J = func_J / x_train.shape[0]
#     gradient = x_train.transpose().dot((diff)) / x_train.shape[0]
#     weights = weights - (alpha * gradient)
for i in range (num_of_iter):
    diff = x_train.dot(weights) - y_train
    func_J = 0.5* ((diff)**2).sum()
    avg_J = func_J / x_train.shape[0]
    gradient = x_train.transpose().dot((diff)) / x_train.shape[0]
    weights = weights - alpha * gradient

    #prediction
    if(i%1000 == 0):
        test_diff = x_test.dot(weights) - y_test
        test_avg_J = 0.5 * ((diff)**2).sum() / x_test.shape[0]
        print test_avg_J
