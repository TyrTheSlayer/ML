from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import gzip
import sys; 
import pickle;

#add the mnist dataset
f = gzip.open('mnist.pkl.gz', 'rb')
if sys.version_info < (3,):
    data = pickle.load(f)
else:
    data = pickle.load(f, encoding='bytes')
f.close()
(X_train_init, y_train), (X_test_init, y_test) = data
X_train = np.zeros((60000, 784), dtype = int)
X_test = np.zeros((10000, 784), dtype = int)
for i in range(59999):
    X_train[i] = X_train_init[i].flatten()
for i in range(9999):
    X_test[i] = X_test_init[i].flatten()
#make each of the models
#euclidean
euc_knn_1 = KNeighborsClassifier(n_neighbors=1, metric='euclidean').fit(X_train, y_train)
euc_knn_5 = KNeighborsClassifier(n_neighbors=5, metric='euclidean').fit(X_train, y_train)
euc_knn_10 = KNeighborsClassifier(n_neighbors=10, metric='euclidean').fit(X_train, y_train)
#manhattan
man_knn_1 = KNeighborsClassifier(n_neighbors=1, metric='manhattan').fit(X_train, y_train)
man_knn_5 = KNeighborsClassifier(n_neighbors=5, metric='manhattan').fit(X_train, y_train)
man_knn_10 = KNeighborsClassifier(n_neighbors=10, metric='manhattan').fit(X_train, y_train)
#cosine
cos_knn_1 = KNeighborsClassifier(n_neighbors=1, metric='cosine').fit(X_train, y_train)
cos_knn_5 = KNeighborsClassifier(n_neighbors=5, metric='cosine').fit(X_train, y_train)
cos_knn_10 = KNeighborsClassifier(n_neighbors=10, metric='cosine').fit(X_train, y_train)

#training predictions
euc_pred_1_train = euc_knn_1.predict(X_train)
euc_pred_5_train = euc_knn_5.predict(X_train)
euc_pred_10_train = euc_knn_10.predict(X_train)
man_pred_1_train = man_knn_1.predict(X_train)
man_pred_5_train = man_knn_5.predict(X_train)
man_pred_10_train = man_knn_10.predict(X_train)
cos_pred_1_train = cos_knn_1.predict(X_train)
cos_pred_5_train = cos_knn_5.predict(X_train)
cos_pred_10_train = cos_knn_10.predict(X_train)
#test predictions
euc_pred_1_test = euc_knn_1.predict(X_test)
euc_pred_5_test = euc_knn_5.predict(X_test)
euc_pred_10_test = euc_knn_10.predict(X_test)
man_pred_1_test = man_knn_1.predict(X_test)
man_pred_5_test = man_knn_5.predict(X_test)
man_pred_10_test = man_knn_10.predict(X_test)
cos_pred_1_test = cos_knn_1.predict(X_test)
cos_pred_5_test = cos_knn_5.predict(X_test)
cos_pred_10_test = cos_knn_10.predict(X_test)

#print training confusion matrices
print("Training")
print("Manhattan Confusion Matrix Training")
print("1 neighbor")
confusion_matrix = pd.crosstab(y_train, man_pred_1_train, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n")
print("5 neighbors")
confusion_matrix = pd.crosstab(y_train, man_pred_5_train, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n")
print("10 neighbors")
confusion_matrix = pd.crosstab(y_train, man_pred_10_train, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n")

print("Euclidean Confusion Matrix Training")
print("1 neighbor")
confusion_matrix = pd.crosstab(y_train, euc_pred_1_train, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n")
print("5 neighbors")
confusion_matrix = pd.crosstab(y_train, euc_pred_5_train, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n")
print("10 neighbors")
confusion_matrix = pd.crosstab(y_train, euc_pred_10_train, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n")

print("Cosine Confusion Matrix Training")
print("1 neighbor")
confusion_matrix = pd.crosstab(y_train, cos_pred_1_train, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n")
print("5 neighbors")
confusion_matrix = pd.crosstab(y_train, cos_pred_5_train, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n")
print("10 neighbors")
confusion_matrix = pd.crosstab(y_train, cos_pred_10_train, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n\n")

#print testing confusion matrices
print("Testing")
print("Manhattan Confusion Matrix Training")
print("1 neighbor")
confusion_matrix = pd.crosstab(y_test, man_pred_1_test, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n")
print("5 neighbors")
confusion_matrix = pd.crosstab(y_test, man_pred_5_test, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n")
print("10 neighbors")
confusion_matrix = pd.crosstab(y_test, man_pred_10_test, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n")

print("Euclidean Confusion Matrix Training")
print("1 neighbor")
confusion_matrix = pd.crosstab(y_test, euc_pred_1_test, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n")
print("5 neighbors")
confusion_matrix = pd.crosstab(y_test, euc_pred_5_test, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n")
print("10 neighbors")
confusion_matrix = pd.crosstab(y_test, euc_pred_10_test, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n")

print("Cosine Confusion Matrix Training")
print("1 neighbor")
confusion_matrix = pd.crosstab(y_test, cos_pred_1_test, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n")
print("5 neighbors")
confusion_matrix = pd.crosstab(y_test, cos_pred_5_test, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n")
print("10 neighbors")
confusion_matrix = pd.crosstab(y_test, cos_pred_10_test, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n")


neighbors = np.array([1, 5, 10])
#set up arrays for plotting
euc_training = np.array([euc_knn_1.score(X_train, y_train)*100, euc_knn_5.score(X_train, y_train)*100, euc_knn_10.score(X_train, y_train)*100])
man_training = np.array([man_knn_1.score(X_train, y_train)*100, man_knn_5.score(X_train, y_train)*100, man_knn_10.score(X_train, y_train)*100])
cos_training = np.array([cos_knn_1.score(X_train, y_train)*100, cos_knn_5.score(X_train, y_train)*100, cos_knn_10.score(X_train, y_train)*100])
#training
euc_testing = np.array([euc_knn_1.score(X_test, y_test)*100, euc_knn_5.score(X_test, y_test)*100, euc_knn_10.score(X_test, y_test)*100])
man_testing = np.array([man_knn_1.score(X_test, y_test)*100, man_knn_5.score(X_test, y_test)*100, man_knn_10.score(X_test, y_test)*100])
cos_testing = np.array([cos_knn_1.score(X_test, y_test)*100, cos_knn_5.score(X_test, y_test)*100, cos_knn_10.score(X_test, y_test)*100])
#plots
plt.subplot(1, 2, 1) # row 1, col 2 index 1
plt.plot(neighbors, euc_testing, label = 'Euclidean')
plt.plot(neighbors, man_testing, label = 'Manhattan')
plt.plot(neighbors, cos_testing, label = 'Cosine')
plt.legend()
plt.xlabel('n_neighbors')
plt.ylabel('percent correct')
plt.title('Percent Correct per Neighbor Testing')

plt.subplot(1, 2, 2) # index 2
plt.plot(neighbors, euc_training, label = 'Euclidean')
plt.plot(neighbors, man_training, label = 'Manhattan')
plt.plot(neighbors, cos_training, label = 'Cosine')
  
plt.legend()
plt.xlabel('n_neighbors')
plt.ylabel('percent correct')
plt.title('Percent Correct per Neighbor Testing')
plt.show()