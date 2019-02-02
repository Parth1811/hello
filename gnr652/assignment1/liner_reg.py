 #! /usr/bin/python
import numpy as np

#GLOBAL VARIABLES
NUM_OF_ITER = 50000
NUM_OF_BATCHES = 10
ALPHA = 0.005
LAMBDA = 0.1
TRAIN_DATA_SIZE = 108

batch_results = []
data_filepath = 'data/data.csv'


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

def train_gradient(x_train, y_train, weights):
    '''
    This funcntion computes the weights using the gradient decent
    algorithm on the trainning data x_train and y_train
    '''
    for i in range (NUM_OF_ITER):
        loss = Loss(x_train, y_train, weights)
        grad = gradient(x_train, y_train, weights)
        weights -= ALPHA * gradient(x_train, y_train, weights)

        # if(i == 0 or i==NUM_OF_ITER-1):
        #     test_loss = Loss(x_test, y_test, weights)
        #     print loss
        #     print test_loss
        #     print '--------------'

    return loss, weights

if __name__ == '__main__':
    data = get_data()
    x_train, y_train, x_test, y_test = partition_test_train_data(data)

    #Initializing weights to random values
    weights = np.random.rand(18)

    #iterating for different batches
    for batch_id in range(NUM_OF_BATCHES):
        loss, weights = train_gradient(x_train, y_train, weights)
        test_loss = Loss(x_test, y_test, weights)
        print 'Ongoing batch : %d of %d' % (batch_id + 1, NUM_OF_BATCHES)
        print 'Train loss : %f Test loss : %f' % (loss, test_loss)
        print "--------------"
        batch_results.append(test_loss)

        #repartitioning test and train data
        x_train, y_train, x_test, y_test = partition_test_train_data(data)

    print 'Average Loss on Test data : %f ' % (np.array(batch_results).sum()/NUM_OF_BATCHES)
