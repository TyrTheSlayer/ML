from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Loading data
irisData = load_iris()

# Create feature and target arrays
X = irisData.data
y = irisData.target

# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

K = range(1,16)
J = range(0,15)
distortions = []
labels = []
train_pred = []
test_pred = []
centroids =[]

for k in K:
    kmeanModel = KMeans(n_clusters=k).fit(X_train,y_train)
    distortions.append(kmeanModel.inertia_)
    labels.append(kmeanModel.labels_)
    train_pred.append(kmeanModel.predict(X_train))
    test_pred.append(kmeanModel.predict(X_test))
    centroids.append(kmeanModel.cluster_centers_)

for k in J:
    print(k+1, end = "\n")
    #print(centroids[k],end = "\n")
    #print(labels[k],end = "\n")
    print(train_pred, end = "\n")

print(y_train)

#plt.figure()
#plt.plot(K, distortions, 'bx-')
#plt.xlabel('k')
#plt.ylabel('Distortion')
#plt.title('The Elbow Method showing the optimal k')
#plt.show()
