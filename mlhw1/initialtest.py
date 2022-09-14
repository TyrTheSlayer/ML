from math import sqrt
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

def man_dist(x1, x2):
  return abs(x1-x2)

def man_process(row, average_dataset, val):
  return man_dist(row['sepallength'], average_dataset['sepallength'][val]) + man_dist(row['sepalwidth'], average_dataset['sepalwidth'][val]) + man_dist(row['petalwidth'], average_dataset['petalwidth'][val]) + man_dist(row['petallength'], average_dataset['petallength'][val])

df = pd.read_csv("iris_csv.csv")

# X = df.iloc[:, :-1]
# y = df.iloc[:, -1]

# # split the dataset
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=0)

#split the dataset randomly into a 70:30 training to test
ind = np.arange(df.shape[0])
np.random.shuffle(ind)
X_train = df.iloc[ind[:int(0.7*df.shape[0])],:]
X_test = df.iloc[ind[int(0.7*df.shape[0]):],:]

#group by the class for easy parsing
datasets = {}
by_class = X_train.groupby('class')
for groups, data in by_class:
    datasets[groups] = data

#get an average for each feature for each plant
#versicolor
versi_sl_avg = datasets['Iris-versicolor']['sepallength'].mean()
versi_sw_avg = datasets['Iris-versicolor']['sepalwidth'].mean()
versi_pw_avg = datasets['Iris-versicolor']['petalwidth'].mean()
versi_pl_avg = datasets['Iris-versicolor']['sepallength'].mean()
#setosa
setos_sl_avg = datasets['Iris-setosa']['sepallength'].mean()
setos_sw_avg = datasets['Iris-setosa']['sepalwidth'].mean()
setos_pw_avg = datasets['Iris-setosa']['petalwidth'].mean()
setos_pl_avg = datasets['Iris-setosa']['sepallength'].mean()
#virginica
virgi_sl_avg = datasets['Iris-virginica']['sepallength'].mean()
virgi_sw_avg = datasets['Iris-virginica']['sepalwidth'].mean()
virgi_pw_avg = datasets['Iris-virginica']['petalwidth'].mean()
virgi_pl_avg = datasets['Iris-virginica']['sepallength'].mean()

data = {'class':['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'],'sepallength':[setos_sl_avg,versi_sl_avg,virgi_sl_avg],'sepalwidth':[setos_sw_avg,versi_sw_avg,virgi_sw_avg],'petalwidth':[setos_pw_avg,versi_pw_avg,virgi_pw_avg],'petallength':[setos_pl_avg,versi_pl_avg,virgi_pl_avg]}
average_dataset = pd.DataFrame(data)
#For each data point in the training set, find the closest from the average templates. Use Manhattan, Euclidean and Cosine distances (note that higher cosine value means lower distance). Give the point that label.
manhattan = X_train
euclid = X_train
cosin = X_train
for index, row in X_train.iterrows():
  #manhattan
  man_setos = man_process(row, average_dataset, 0)
  man_versi = man_process(row, average_dataset, 1)
  man_virgi = man_process(row, average_dataset, 2)
  if (man_setos < man_versi) and (man_setos < man_virgi):
    manhattan['class'] = manhattan['class'].replace([index],'Iris-setosa')