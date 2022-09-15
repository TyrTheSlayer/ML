from math import sqrt
import numpy as np
from numpy.linalg import norm
import pandas as pd
import gzip
import sys; 
import pickle;
import numpy_indexed as npi

def man_calculation(means, x_train):
  total = 0
  for i in range(28):
    for j in range(28):
      total += abs(means[i][j] - x_train[i][j])
  return total

def euc_calc(means, x_train):
  total = 0
  for i in range(28):
    for j in range(28):
      total += pow((means[i][j] - x_train[i][j]), 2)
  return sqrt(total)

def cos_calc(means, x_train):
  A = np.array(means).flatten()
  B = np.array(x_train).flatten()
  return np.dot(A,B)/(norm(A)*norm(B))

#add the mnist dataset
f = gzip.open('mnist.pkl.gz', 'rb')
if sys.version_info < (3,):
    data = pickle.load(f)
else:
    data = pickle.load(f, encoding='bytes')
f.close()
(x_train, y_train), (x_test, y_test) = data

#generate average datapoints (provided by numpy)
digits, means = npi.group_by(y_train).mean(x_train)

man_train = np.zeros(60000, dtype = int)
man_test = np.zeros(10000, dtype = int)
euc_train = np.zeros(60000, dtype = int)
euc_test = np.zeros(10000, dtype = int)
cos_train = np.zeros(60000, dtype = int)
cos_test = np.zeros(10000, dtype = int)
man_avg = np.zeros(10, dtype=int)
euc_avg = np.zeros(10, dtype=int)
cos_avg = np.zeros(10, dtype=int)
#find distances
for i in range(x_train.size):
  for image in range(9):
    #manhattan
    man_avg[image] = man_calculation(means[image], x_train[i])
    #euclidean
    euc_avg[image] = euc_calc(means[image], x_train[i])
    #cosine
    cos_avg[image] = cos_calc(means[image], x_train[i])
  #find the proper label as min from list
  man_train[i] = man_avg.argmin()
  euc_train[i] = euc_avg.argmin()
  cos_train[i] = cos_avg.argmax()
  #do the same with test set
for i in range(x_test.size):
  for image in range(9):
    #manhattan
    man_avg[image] = man_calculation(means[image], x_test[i])
    #euclidean
    euc_avg[image] = euc_calc(means[image], x_test[i])
    #cosine
    cos_avg[image] = cos_calc(means[image], x_test[i])
  #find the proper label as min from list
  man_test[i] = man_avg.argmin()
  euc_test[i] = euc_avg.argmin()
  cos_test[i] = cos_avg.argmax()

#print training confusion matrices
print("Training")
print("Manhattan Confusion Matrix Training")
confusion_matrix = pd.crosstab(y_train, man_train, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n\n")

print("Euclidean Confusion Matrix Training")
confusion_matrix = pd.crosstab(y_train, euc_train, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n\n")

print("Cosine Confusion Matrix Training")
confusion_matrix = pd.crosstab(y_train, cos_train, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n\n")

#print testing confusion matrices
print("Testing")
print("Manhattan Confusion Matrix Training")
confusion_matrix = pd.crosstab(y_test, man_test, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n\n")

print("Euclidean Confusion Matrix Training")
confusion_matrix = pd.crosstab(y_test, euc_test, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n\n")

print("Cosine Confusion Matrix Training")
confusion_matrix = pd.crosstab(y_test, cos_test, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n\n")