 #! /usr/bin/python
import numpy as np
import matplotlib.pyplot as plt


#GLOBAL VARIABLES
NUM_OF_ITER = 500000
LOG_DATA = 1000
NUM_OF_BATCHES = 10
ALPHA = 0.005
LAMBDA = 0.1
TRAIN_DATA_SIZE = 108

data_filepath = 'data/data.csv'

train_loss_history = {
    'grad_dec' : [],
    'closed_reg' : []
}
test_loss_history = {
    'grad_dec' : [],
    'closed_reg' : []
}


def get_data():
    '''
    This function load the data from the csv file
    and return a array padded with one and the top most
    title row removed
    '''
    # data = open(data_filepath, 'w').readlines()
    data = np.genfromtxt(data_filepath, delimiter=',')
    data = np.array(data[1:])
    data_array = np.ones((data.shape[0], data.shape[1]+1))
    data_array[:,1:] = data
    return data_array

def partition_test_train_data(data, shuffle = True):
    '''
    This function create the trainning and testing
    sets with the given data
    '''
    if shuffle:
        np.random.shuffle(data)
    x_train = data[:TRAIN_DATA_SIZE,:-1]
    y_train = data[:TRAIN_DATA_SIZE,-1]
    x_test = data[TRAIN_DATA_SIZE:,:-1]
    y_test = data[TRAIN_DATA_SIZE:,-1]

    return x_train, y_train, x_test, y_test

def Loss(X, Y, W):
    '''
    This is the Loss(J) function which takes the X, Y, W matrices
    as input and computes and return the coressponding loss
    '''
    diff = X.dot(W) - Y
    func_J = 0.5* ((diff**2).sum() + LAMBDA* W.transpose().dot(W))
    avg_J = func_J / X.shape[0]
    return avg_J

def gradient(X, Y, W):
    '''
    This functions computes the garident of the above Loss function
    '''
    grad = X.transpose().dot(X.dot(W) - Y) + (LAMBDA * W)
    grad /= X.shape[0]
    return grad

def train_gradient(X, Y, W):
    '''
    This funcntion computes the weights using the gradient decent
    algorithm on the trainning data x_train and y_train
    '''
    for i in range (NUM_OF_ITER):
        loss = Loss(X, Y, W)
        grad = gradient(X, Y, W)
        W -= ALPHA * grad

        if (i % LOG_DATA == 0):
            train_loss_history['grad_dec'].append(loss)

    return loss, W

def train_closed_reg(X, Y, tries=10):
    failed = False
    try:
        W = np.dot((np.linalg.inv(np.dot(X.transpose(),X))),np.dot(X.transpose(),Y))
        loss = Loss(X, Y, W)
    except:
        #Handling the singular matrix cases
        failed = True
        W, loss = np.random.rand(18), 0
    # print W

    return loss, W, failed




if __name__ == '__main__':
    data = get_data()
    x_train, y_train, x_test, y_test = partition_test_train_data(data)

    #Initializing weights to random values
    weights_grad = np.random.rand(18)

    #iterating for different batches
    for batch_id in range(NUM_OF_BATCHES):
        #Finding weights using gradient decent
        loss_grad, weights_grad = train_gradient(x_train, y_train, weights_grad)

        #Finding wieghts using closed regression
        closed_failed, counter = True, 0
        while closed_failed:
            loss_closed , weights_closed, closed_failed  = train_closed_reg(x_train, y_train)
            # loss_closed, weights_closed = train_gradient(x_train, y_train, weights_closed)
            x_train, y_train, x_test, y_test = partition_test_train_data(data)
            counter += 1
            if counter > 100:
                print "Unavle to do Closed Regression"
                break

        #Finding average loss on test data
        test_loss_grad = Loss(x_test, y_test, weights_grad)
        test_loss_closed = Loss(x_test, y_test, weights_closed)
        test_loss_history['grad_dec'].append(test_loss_grad)
        test_loss_history['closed_reg'].append(test_loss_closed)

        print 'Ongoing batch : %d of %d' % (batch_id + 1, NUM_OF_BATCHES)
        print 'Gradient Decent  - train_loss: %.4f test_loss: %.4f' % (loss_grad, test_loss_grad)
        print 'Closed Regression- train_loss: %.4f test_loss: %.4f tries: %d' % (loss_closed, test_loss_closed, counter)
        print "--------------"

        #repartitioning test and train data
        x_train, y_train, x_test, y_test = partition_test_train_data(data)



    plt.plot(test_loss_history['grad_dec'])
    plt.plot(test_loss_history['closed_reg'])
    plt.show()
    # print 'Average Loss on Test data : %f ' % (np.array(batch_results).sum()/NUM_OF_BATCHES)
