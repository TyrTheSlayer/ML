from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def label_centroids(correct_labels, closest_centroid, k):
    correct_centroid_labels = []
    K = range(0, k)
    for i in K:
        tmp = []
        for p in range(0,3):
            tmp.append(0)
        for j in range(0,len(closest_centroid)):
            if (closest_centroid[j] == i):
                tmp[correct_labels[j]] += 1
        correct_centroid_labels.append(tmp.index(max(tmp)))
    #print(correct_centroid_labels)
    return correct_centroid_labels

def get_pred(closest_centroid, correct_centroid_labels):
    prediction = []
    for j in range(0, len(closest_centroid)):
        prediction.append(correct_centroid_labels[closest_centroid[j]])

    return prediction


# Loading data
irisData = load_iris()

# Create feature and target arrays
X = irisData.data
y = irisData.target

# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

K = range(1, 16)
J = range(0, 15)
distortions = []
labels = []
train_pred = []
test_pred = []
centroids = []

for k in K:
    kmeanModel = KMeans(n_clusters=k).fit(X_train, y_train)
    distortions.append(kmeanModel.inertia_)
    labels.append(kmeanModel.labels_)
    train_pred.append(kmeanModel.predict(X_train))
    test_pred.append(kmeanModel.predict(X_test))
    centroids.append(kmeanModel.cluster_centers_)

#for k in J:
    #print(k + 1, end="\n")
    # print(centroids[k],end = "\n")
    #print(labels[k],end = "\n")
    #print(train_pred[k], end = "\n")
for k in K:
    centroid_labels = label_centroids(y_train, labels[k-1], k)
    pred = get_pred(train_pred[k-1],centroid_labels)
    print(k, end = " cluster ")
    print("Training", end = "\n")
    confusion_matrix = pd.crosstab(y_train, pred, rownames=['Actual'], colnames=['Predicted'])
    print(confusion_matrix)
    print("----------------------", end = "\n")

    pred = get_pred(test_pred[k - 1], centroid_labels)
    print(k, end = " cluster ")
    print("Testing", end = "\n")
    confusion_matrix = pd.crosstab(y_test, pred, rownames=['Actual'], colnames=['Predicted'])
    print(confusion_matrix)
    print("----------------------", end="\n")
# print(y_train)

# plt.figure()
# plt.plot(K, distortions, 'bx-')
# plt.xlabel('k')
# plt.ylabel('Distortion')
# plt.title('The Elbow Method showing the optimal k')
# plt.show()
