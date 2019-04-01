import matplotlib.pyplot as plt
import numpy as np
import scipy.io

IMAGE_SIZE      = (145, 145)
NO_OF_CHANNELS  = 200
NO_OF_CLASSES   = 16
NUM_OF_ITER = 500
LOG_DATA = 1
train_loss_history = []
alpha = 1

#Loading data
data            = scipy.io.loadmat('data/Indian_pines.mat')['indian_pines']                          #(145,145,220)
corrected_data  = scipy.io.loadmat('data/Indian_pines_corrected.mat')['indian_pines_corrected']      #(145,145,200)
ground_truth    = scipy.io.loadmat('data/Indian_pines_gt.mat')['indian_pines_gt']                    #(145,145)


#Doing one hot encoding for ground truth
# onehot_ground_truth = np.zeros((IMAGE_SIZE[0],IMAGE_SIZE[1],NO_OF_CLASSES+1))
# for i in range(IMAGE_SIZE[0]):
#     for j in range(IMAGE_SIZE[1]):
#         onehot_ground_truth[i,j,ground_truth[i,j]] = 1

#assigning X and Y
X = corrected_data.reshape((IMAGE_SIZE[0] * IMAGE_SIZE[1], 200))
Y = ground_truth.reshape((IMAGE_SIZE[0] * IMAGE_SIZE[1]))

#normalizing X
X = (X - np.mean(X)) / (np.max(X) - np.min(X))

#Removing the dont care examples
dont_care_list = []
for i in range(X.shape[0]):
    if Y[i] == 0:
        dont_care_list.append(i)

X = np.delete(X, dont_care_list, 0)
Y = np.delete(Y, dont_care_list, 0)

#Sorting the data as per the ground truth so that exactly half examples
#from each class will bbe present in the training and testing data
X = X.transpose((1, 0))
Y = Y.reshape((1, Y.size))
sorting_array = np.append(Y, X, axis=0)
sorting_array = sorting_array.transpose((1, 0))
sorted_array = sorting_array[sorting_array[:,0].argsort()]

#seperating training and testing data
X_train = np.zeros((sorted_array.shape[0]/2, NO_OF_CHANNELS + 1))
X_test = np.zeros((sorted_array.shape[0]/2, NO_OF_CHANNELS + 1))
for i in range(sorted_array.shape[0]/2):
    X_train[i] = sorted_array[2*i]
    X_test[i] = sorted_array[2*i + 1]

Y_train = X_train[:,0]      #extracting output label from xtrain
Y_test = X_test[:,0]        #extracting output label from xtest
X_train = X_train[:,1:]     #slicing of the output axis from xtrain
X_test = X_test[:,1:]       #slicing of the output axis from xtest

# print X_train.shape
# print X_test.shape
# print Y_train.shape
# print Y_test.shape

def predict(X_train, Y_train, W):
    Z = X_train.dot(W)
    exp_Z = np.exp(Z)
    total_exp_Z = np.transpose(exp_Z.sum(axis=1)).reshape((exp_Z.shape[0],1))
    YHAT_train = exp_Z / total_exp_Z
    YPRED = np.zeros(Y_train.shape)
    for i in range(Y_train.shape[0]):
        YPRED[i] = YHAT_train[i, int(Y_train[i]) - 1]
    return YPRED, YHAT_train

def entropy(YPRED):
    entropy = -(np.log(YPRED))

def gradient_decent(X_train, Y_train, YHAT_train):
    grad_mat = np.zeros((YHAT_train.shape[0], NO_OF_CLASSES))
    for i in range(YHAT_train.shape[0]):
        for j in range(16):
            if j == int(Y_train[i] ) - 1:
                grad_mat[i][j] += YHAT_train[i][j] - 1
            else:
                grad_mat[i][j] += 0#YHAT_train[i][j]
    grad = X_train.transpose().dot(grad_mat)
    return grad / X_train.shape[0] * alpha

##################TRAINING##########################
W = np.random.random_sample((NO_OF_CHANNELS, NO_OF_CLASSES))

for i in range(NUM_OF_ITER):
    YPRED, YHAT_train = predict(X_train, Y_train, W)
    grad = gradient_decent(X_train, Y_train, YHAT_train)
    loss = np.sum(-(np.log(YPRED)),axis=0) / Y_train.shape[0]
    if (i % LOG_DATA == 0):
        train_loss_history.append(loss)
    W += (grad * W)
    print ("Done iter no --" + str(i) + "--")
