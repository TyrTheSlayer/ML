from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import gzip
import sys
import pickle
from numpy.linalg import norm
from math import sqrt

def label_centroids(correct_labels, closest_centroid, k):
    correct_centroid_labels = []
    K = range(0, k)
    for i in K:
        tmp = []
        for p in range(0,10):
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
        for j in range(0,28):
           val += abs(centroids[i][j] - data[j])
        if val < min:
            min = val
            index = i
    return index

def euc_distance(centroids,data):
    min = 9999999
    for i in range(0, len(centroids)):
        val = 0
        for j in range(0,28):
            val += pow(centroids[i][j] - data[j],2)
        if sqrt(val) < min:
            min = val
            index = i
    return index

def cos_distance(centroids,data):
    max = 0
    for i in range(0, len(centroids)):
        A = np.array([centroids[i][0], centroids[i][1], centroids[i][2], centroids[i][3]])
        B = np.array([data[0], data[1], data[2], data[3]])
        val = np.dot(A, B) / (norm(A) * norm(B))
        if val > max:
            max = val
            index = i
    return index

def score(actual, predicted):
    num = 0
    for i in range(0,len(actual)):
        if actual[i] != predicted[i]:
            num += 1
    return num / len(actual)


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
X_train = X_train[0:2500]
X_test = np.zeros((10000, 784), dtype = int)
X_test = X_test[0:200]
y_train = y_train[0:2500]
y_test = y_test[0:200]

for i in range(2500):
    X_train[i] = x_train[i].flatten()
for i in range(200):
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

man_distances_train = []
euc_distances_train = []
#cos_distances_train = []

man_distances_test = []
euc_distances_test = []
#cos_distances_test = []

for i in range(0,len(centroids)):
    tmp_man = []
    tmp_euc = []
    #tmp_cos = []

    tmp1_man = []
    tmp1_euc = []
    #tmp1_cos = []

    for j in range(0, len(X_train)):
        tmp_man.append(man_distance(centroids[i], X_train[j]))
        tmp_euc.append(euc_distance(centroids[i], X_train[j]))
        #tmp_cos.append(cos_distance(centroids[i], X_train[j]))

    for j in range(0, len(X_test)):
        tmp1_man.append(man_distance(centroids[i], X_test[j]))
        tmp1_euc.append(euc_distance(centroids[i], X_test[j]))
        #tmp1_cos.append(cos_distance(centroids[i], X_test[j]))

    man_distances_train.append(tmp_man)
    euc_distances_train.append(tmp_euc)
    #cos_distances_train.append(tmp_cos)

    man_distances_test.append(tmp1_man)
    euc_distances_test.append(tmp1_euc)
    #cos_distances_test.append(tmp1_cos)

#print(man_distances)
#print(euc_distances)
#print(cos_distances)

#for k in J:
    #print(k + 1, end="\n")
    # print(centroids[k],end = "\n")
    #print(labels[k],end = "\n")
    #print(train_pred[k], end = "\n")
man_score = []
euc_score = []
cos_score = []

for k in K:
    centroid_labels = label_centroids(y_train, labels[k-1], k)
    print(centroid_labels)

    pred = get_pred(man_distances_train[k-1],centroid_labels)
    print(k, end = " cluster ")
    print("Manhattan Training", end = "\n")
    confusion_matrix = pd.crosstab(y_train, pred, rownames=['Actual'], colnames=['Predicted'])
    print(confusion_matrix)
    print("----------------------", end = "\n")

    pred = get_pred(euc_distances_train[k - 1], centroid_labels)
    print(k, end=" cluster ")
    print("Euclidean Training", end="\n")
    confusion_matrix = pd.crosstab(y_train, pred, rownames=['Actual'], colnames=['Predicted'])
    print(confusion_matrix)
    print("----------------------", end="\n")

    #pred = get_pred(cos_distances_train[k - 1], centroid_labels)
    #print(k, end=" cluster ")
    #print("Cosine Training", end="\n")
    #confusion_matrix = pd.crosstab(y_train, pred, rownames=['Actual'], colnames=['Predicted'])
    #print(confusion_matrix)
    #print("----------------------", end="\n")

    pred = get_pred(man_distances_test[k - 1], centroid_labels)
    print(k, end=" cluster ")
    print("Manhattan Testing", end="\n")
    confusion_matrix = pd.crosstab(y_test, pred, rownames=['Actual'], colnames=['Predicted'])
    print(confusion_matrix)
    print("----------------------", end="\n")
    man_score.append(score(y_test, pred))

    pred = get_pred(euc_distances_test[k - 1], centroid_labels)
    print(k, end=" cluster ")
    print("Euclidean Testing", end="\n")
    confusion_matrix = pd.crosstab(y_test, pred, rownames=['Actual'], colnames=['Predicted'])
    print(confusion_matrix)
    print("----------------------", end="\n")
    euc_score.append(score(y_test, pred))

    #pred = get_pred(cos_distances_test[k - 1], centroid_labels)
    #print(k, end=" cluster ")
    #print("Cosine Testing", end="\n")
    #confusion_matrix = pd.crosstab(y_test, pred, rownames=['Actual'], colnames=['Predicted'])
    #print(confusion_matrix)
    #print("----------------------", end="\n")
    #cos_score.append(score(y_test, pred))

plt.plot(K, euc_score, label='Euclidean')
plt.plot(K, man_score, label='Manhattan')
#plt.plot(K, cos_score, label='Cosine')

plt.legend()
plt.xlabel('k value')
plt.ylabel('percent correct')
plt.title('Percent Correct per Neighbor Testing')
plt.show()