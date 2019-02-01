 #! /usr/bin/python
import numpy as np


data_filepath = 'data/data.csv'
num_of_iter = 500000
num_of_batch = 10
alpha = 0.005
lamba = 0.1

batch_results = []

# data = open(data_filepath, 'w').readlines()
data = np.genfromtxt(data_filepath, delimiter=',')
data = np.array(data[1:])
data_array = np.ones((data.shape[0], data.shape[1]+1))
data_array[:,1:] = data
data = data_array

for j in range(num_of_batch):
    x_train = data[:108,:-1]
    y_train = data[:108,-1]
    x_test = data[108:,:-1]
    y_test = data[108:,-1]


    weights = np.random.rand(18)

    for i in range (num_of_iter):
        diff = x_train.dot(weights) - y_train
        func_J = 0.5* (((diff)**2).sum() + lamba* weights.transpose().dot(weights))
        avg_J = func_J / x_train.shape[0]
        gradient = (x_train.transpose().dot((diff)) + lamba * weights) / x_train.shape[0]
        weights = weights - alpha * gradient
        # weights = np.random.rand(18)

        #prediction
        if(i == 0 or i==num_of_iter-1):
            test_diff = x_test.dot(weights) - y_test
            test_avg_J = 0.5 * (((diff)**2).sum() + lamba* weights.transpose().dot(weights)) / x_test.shape[0]
            print avg_J
            print test_avg_J
            print '--------------'

    batch_results.append((avg_J, test_avg_J))
    np.random.shuffle(data)

batch_avg_J = 0
for result in batch_results:
    batch_avg_J += result[1]
print ("-----------"+str(batch_avg_J/num_of_batch)+"--------------")
