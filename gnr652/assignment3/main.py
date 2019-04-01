import numpy as np
import scipy.io

IMAGE_SIZE      = (145, 145)
NO_OF_CHANNELS  = 200
NO_OF_CLASSES   = 16

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

print X_train.shape
print X_test.shape
print Y_train.shape
print Y_test.shape
