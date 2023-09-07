import csv
import numpy as np
filepath ="/home/dipesh/Desktop/Acads/mine/GNR652/asmt1/gnr_data/data1.csv"
myFile = np.genfromtxt(filepath, delimiter=',')

myFile=myFile[1:]
norm_fact = [27,4,5,1,3,2,1,1,1,4,1,7,1,8,1,4,1,23.4]
norm_fact = np.array(norm_fact)
myFile = myFile/norm_fact
# print(np.sum(myFile))
# print(myFile[:,:])
X_train=myFile[:108,:-1]
Y_train=myFile[:108,17]
X_test=myFile[108:,:-1]
Y_test=myFile[108:,17]

# print(norm_fact.shape)
print("\n####  Data Shapes  ####\n")
print("MyData_shape =",myFile.shape)
print("X_train_shape =",X_train.shape,"Y_train_shape =",Y_train.shape)
print("X_test_shape =",X_test.shape,"X_test_shape =",Y_test.shape)
print("\n#####  Actual Program  #####\n\n")

W1 = X_train.transpose().dot(X_train.dot(X_train.transpose())).dot(Y_train)
print(W1.shape)
y_pred1=X_test.dot(W1)
diff= y_pred1 - Y_test
# print(X_test.dot(W)-Y_test)

# W2 = (X_train.transpose().dot(X_train)).dot(X_train.transpose()).dot(Y_train)
# y_pred2=X_test.dot(W2)
# diff2=y_pred2 - Y_test

# print(W1-W2)
# print(diff2)

# Loss function
# W1 = np.random.rand(17,1)
alpha = 0.001
num_iter = 100000
lamb_penalty = 0.1
def loss_n_grad(X_train,Y_train,W1,alpha):
	J= (X_train.dot(W1) - Y_train)
	J = J.dot(J.transpose())
	J = 0.5* np.sum(J) + lamb_penalty * np.sum(W1*W1)
	J/= X_train.shape[0]

	# print "loss : ",J
	grads_W =X_train.transpose().dot((X_train.dot(W1) - Y_train)) + 2*lamb_penalty*W1
	return J,grads_W


loss =0
grad = 0
loss , grad = loss_n_grad(X_train,Y_train,W1,alpha)
print("loss : ",loss)

# For optimizing W
for i in range(num_iter):
	loss , grad = loss_n_grad(X_train,Y_train,W1,alpha)
	W1 = W1 - alpha * grad
	if(i%5000==0):
		print(loss)

y_pred1=X_test.dot(W1)
diff= y_pred1 - Y_test
loss_test, g = loss_n_grad(X_test,Y_test,W1,alpha)
print("loss_test : ",loss_test)
# print(W1)
print(diff)
acc = np.sum(abs(diff) / Y_test) *100 /27
print("accuracy :",acc)