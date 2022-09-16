from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import gzip
import sys; 
import pickle;

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

def man_distance(centroids, data):
    min = 9999999
    for i in range(0, len(centroids)):
        val = 0
        for j in range(0, 28):
            for k in range(0,28):
                val += abs(centroids[i][j][k] - data[j][k])
        if val < min:
            min = val
            index = i
    return index

# Loading data
#add the mnist dataset
f = gzip.open('mnist.pkl.gz', 'rb')
if sys.version_info < (3,):
    data = pickle.load(f)
else:
    data = pickle.load(f, encoding='bytes')
f.close()
(x_train, y_train), (x_test, y_test) = data

X_train = np.zeros((60000, 784), dtype = int)
X_test = np.zeros((10000, 784), dtype = int)
for i in range(59999):
    X_train[i] = x_train[i].flatten()
for i in range(9999):
    X_test[i] = x_train[i].flatten()

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

man_distances = []
for i in range(0,len(centroids)):
    tmp = []
    for j in range(0, len(X_train)):
        val = man_distance(centroids[i], X_train[j])
        tmp.append(val)
    man_distances.append(tmp)
print(man_distances)

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