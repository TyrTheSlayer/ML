from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import pandas as pd
from math import sqrt
import numpy as np
from numpy.linalg import norm
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

def man_distance(centroids, data):
    min = 9999999
    for i in range(0, len(centroids)):
        #print(i)
        #print(abs(centroids[i][0] - data[0]) + abs(centroids[i][1] - data[1]) + abs(centroids[i][2] - data[2]) + abs(centroids[i][3] - data[3]))
        val = abs(centroids[i][0] - data[0]) + abs(centroids[i][1] - data[1]) + abs(centroids[i][2] - data[2]) + abs(centroids[i][3] - data[3])
        if val < min:
            min = val
            index = i
    return index

def euc_distance(centroids,data):
    min = 9999999
    for i in range(0, len(centroids)):
        val = sqrt(pow(centroids[i][0] - data[0],2) + pow(centroids[i][1] - data[1],2) + pow(centroids[i][2] - data[2],2) + pow(centroids[i][3] - data[3],2))
        if val < min:
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

man_distances_train = []
euc_distances_train = []
cos_distances_train = []

man_distances_test = []
euc_distances_test = []
cos_distances_test = []

for i in range(0,len(centroids)):
    tmp_man = []
    tmp_euc = []
    tmp_cos = []

    tmp1_man = []
    tmp1_euc = []
    tmp1_cos = []

    for j in range(0, len(X_train)):
        tmp_man.append(man_distance(centroids[i], X_train[j]))
        tmp_euc.append(euc_distance(centroids[i], X_train[j]))
        tmp_cos.append(cos_distance(centroids[i], X_train[j]))

    for j in range(0, len(X_test)):
        tmp1_man.append(man_distance(centroids[i], X_test[j]))
        tmp1_euc.append(euc_distance(centroids[i], X_test[j]))
        tmp1_cos.append(cos_distance(centroids[i], X_test[j]))

    man_distances_train.append(tmp_man)
    euc_distances_train.append(tmp_euc)
    cos_distances_train.append(tmp_cos)

    man_distances_test.append(tmp1_man)
    euc_distances_test.append(tmp1_euc)
    cos_distances_test.append(tmp1_cos)

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
    #print(centroid_labels)

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

    pred = get_pred(cos_distances_train[k - 1], centroid_labels)
    print(k, end=" cluster ")
    print("Cosine Training", end="\n")
    confusion_matrix = pd.crosstab(y_train, pred, rownames=['Actual'], colnames=['Predicted'])
    print(confusion_matrix)
    print("----------------------", end="\n")

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

    pred = get_pred(cos_distances_test[k - 1], centroid_labels)
    print(k, end=" cluster ")
    print("Cosine Testing", end="\n")
    confusion_matrix = pd.crosstab(y_test, pred, rownames=['Actual'], colnames=['Predicted'])
    print(confusion_matrix)
    print("----------------------", end="\n")
    cos_score.append(score(y_test, pred))

#print(y_test)
#print(man_distances_test)

plt.plot(K, euc_score, label='Euclidean')
plt.plot(K, man_score, label='Manhattan')
plt.plot(K, cos_score, label='Cosine')

plt.legend()
plt.xlabel('k value')
plt.ylabel('percent correct')
plt.title('Percent Correct per Neighbor Testing')
plt.show()

