 #! /usr/bin/python
import numpy as np


data_filepath = 'data/data.csv'
num_of_iter = 50000
num_of_batch = 10
alpha = 0.005
lamba = 0.1
train_partition = 108

batch_results = []

# data = open(data_filepath, 'w').readlines()
def get_data():
    data = np.genfromtxt(data_filepath, delimiter=',')
    data = np.array(data[1:])
    data_array = np.ones((data.shape[0], data.shape[1]+1))
    data_array[:,1:] = data
    return data_array

def partition_test_train_data(data):
    x_train = data[:train_partition,:-1]
    y_train = data[:train_partition,-1]
    x_test = data[train_partition:,:-1]
    y_test = data[train_partition:,-1]

    return x_train, y_train, x_test, y_test

def Loss(X, Y, W):
    diff = X.dot(W) - Y
    func_J = 0.5* ((diff**2).sum() + lamba* W.transpose().dot(W))
    avg_J = func_J / X.shape[0]
    return avg_J

def gradient(X, Y, W):
    grad = X.transpose().dot(X.dot(W) - Y) + (lamba * W)
    grad /= X.shape[0]
    return grad

def train_gradient(x_train, y_train, weights):
    for i in range (num_of_iter):
        loss = Loss(x_train, y_train, weights)
        grad = gradient(x_train, y_train, weights)
        weights -= alpha * gradient(x_train, y_train, weights)

        # if(i == 0 or i==num_of_iter-1):
        #     test_loss = Loss(x_test, y_test, weights)
        #     print loss
        #     print test_loss
        #     print '--------------'

    return weights

if __name__ == '__main__':
    data = get_data()
    x_train, y_train, x_test, y_test = partition_test_train_data(data)
    weights = np.random.rand(18)
    for batch_id in range(num_of_batch):
        weights = train_gradient(x_train, y_train, weights)
        test_loss = Loss(x_test, y_test, weights)
        print test_loss
        print "--------------"
