from math import sqrt
import pandas as pd
import numpy as np
from numpy.linalg import norm

def man_dist(x1, x2):
  return abs(x1-x2)

def man_process(row, average_dataset, val):
  return man_dist(row['sepallength'], average_dataset['sepallength'][val]) + man_dist(row['sepalwidth'], average_dataset['sepalwidth'][val]) + man_dist(row['petalwidth'], average_dataset['petalwidth'][val]) + man_dist(row['petallength'], average_dataset['petallength'][val])

def euc_process(row, average_dataset, val):
  return sqrt(pow((row['sepallength'] - average_dataset['sepallength'][val]), 2) + pow((row['sepalwidth'] - average_dataset['sepalwidth'][val]), 2) + pow((row['petalwidth'] - average_dataset['petalwidth'][val]), 2) + pow((row['petallength'] - average_dataset['petallength'][val]), 2))

def cos_process(row, average_dataset, val):
  A = np.array([row['sepallength'], row['sepalwidth'], row['petalwidth'], row['petallength']])
  B = np.array([average_dataset['sepallength'][val], average_dataset['sepalwidth'][val], average_dataset['petalwidth'][val], average_dataset['petallength'][val]])
  return np.dot(A,B)/(norm(A)*norm(B))

df = pd.read_csv("iris_csv.csv")

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
versi_pl_avg = datasets['Iris-versicolor']['petallength'].mean()
#setosa
setos_sl_avg = datasets['Iris-setosa']['sepallength'].mean()
setos_sw_avg = datasets['Iris-setosa']['sepalwidth'].mean()
setos_pw_avg = datasets['Iris-setosa']['petalwidth'].mean()
setos_pl_avg = datasets['Iris-setosa']['petallength'].mean()
#virginica
virgi_sl_avg = datasets['Iris-virginica']['sepallength'].mean()
virgi_sw_avg = datasets['Iris-virginica']['sepalwidth'].mean()
virgi_pw_avg = datasets['Iris-virginica']['petalwidth'].mean()
virgi_pl_avg = datasets['Iris-virginica']['petallength'].mean()

data = {'class':['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'],'sepallength':[setos_sl_avg,versi_sl_avg,virgi_sl_avg],'sepalwidth':[setos_sw_avg,versi_sw_avg,virgi_sw_avg],'petalwidth':[setos_pw_avg,versi_pw_avg,virgi_pw_avg],'petallength':[setos_pl_avg,versi_pl_avg,virgi_pl_avg]}
average_dataset = pd.DataFrame(data)
#For each data point in the training set, find the closest from the average templates. Use Manhattan, Euclidean and cos distances (note that higher cos value means lower distance). Give the point that label.
man_train = X_train.copy(deep=True)
euc_train = X_train.copy(deep=True)
cos_train = X_train.copy(deep=True)
for index, row in X_train.iterrows():
  #manhattan
  man_setos = man_process(row, average_dataset, 0)
  man_versi = man_process(row, average_dataset, 1)
  man_virgi = man_process(row, average_dataset, 2)
  if((man_setos < man_versi) and (man_setos < man_virgi)):
    man_train.at[index, 'class']='Iris-setosa'
  if((man_versi < man_setos) and (man_versi < man_virgi)):
    man_train.at[index, 'class'] = 'Iris-versicolor'
  if((man_virgi < man_versi) and (man_virgi < man_setos)):
    man_train.at[index, 'class'] = 'Iris-virginica'
  #euclidean
  euc_setos = euc_process(row, average_dataset, 0)
  euc_versi = euc_process(row, average_dataset, 1)
  euc_virgi = euc_process(row, average_dataset, 2)
  if((euc_setos < euc_versi) and (euc_setos < euc_virgi)):
    euc_train.at[index, 'class']='Iris-setosa'
  if((euc_versi < euc_setos) and (euc_versi < euc_virgi)):
    euc_train.at[index, 'class'] = 'Iris-versicolor'
  if((euc_virgi < euc_versi) and (euc_virgi < euc_setos)):
    euc_train.at[index, 'class'] = 'Iris-virginica'
  #cos
  cos_setos = cos_process(row, average_dataset, 0)
  cos_versi = cos_process(row, average_dataset, 1)
  cos_virgi = cos_process(row, average_dataset, 2)
  if((cos_setos < cos_versi) and (cos_setos < cos_virgi)):
    cos_train.at[index, 'class']='Iris-setosa'
  if((cos_versi < cos_setos) and (cos_versi < cos_virgi)):
    cos_train.at[index, 'class'] = 'Iris-versicolor'
  if((cos_virgi < cos_versi) and (cos_virgi < cos_setos)):
    cos_train.at[index, 'class'] = 'Iris-virginica'

#do the same for test set
man_test = X_test.copy(deep=True)
euc_test = X_test.copy(deep=True)
cos_test = X_test.copy(deep=True)
for index, row in X_test.iterrows():
  #manhattan
  man_setos = man_process(row, average_dataset, 0)
  man_versi = man_process(row, average_dataset, 1)
  man_virgi = man_process(row, average_dataset, 2)
  if((man_setos < man_versi) and (man_setos < man_virgi)):
    man_test.at[index, 'class']='Iris-setosa'
  if((man_versi < man_setos) and (man_versi < man_virgi)):
    man_test.at[index, 'class'] = 'Iris-versicolor'
  if((man_virgi < man_versi) and (man_virgi < man_setos)):
    man_test.at[index, 'class'] = 'Iris-virginica'
  #euclidean
  euc_setos = euc_process(row, average_dataset, 0)
  euc_versi = euc_process(row, average_dataset, 1)
  euc_virgi = euc_process(row, average_dataset, 2)
  if((euc_setos < euc_versi) and (euc_setos < euc_virgi)):
    euc_test.at[index, 'class']='Iris-setosa'
  if((euc_versi < euc_setos) and (euc_versi < euc_virgi)):
    euc_test.at[index, 'class'] = 'Iris-versicolor'
  if((euc_virgi < euc_versi) and (euc_virgi < euc_setos)):
    euc_test.at[index, 'class'] = 'Iris-virginica'
  #cos
  cos_setos = cos_process(row, average_dataset, 0)
  cos_versi = cos_process(row, average_dataset, 1)
  cos_virgi = cos_process(row, average_dataset, 2)
  if((cos_setos < cos_versi) and (cos_setos < cos_virgi)):
    cos_test.at[index, 'class']='Iris-setosa'
  if((cos_versi < cos_setos) and (cos_versi < cos_virgi)):
    cos_test.at[index, 'class'] = 'Iris-versicolor'
  if((cos_virgi < cos_versi) and (cos_virgi < cos_setos)):
    cos_test.at[index, 'class'] = 'Iris-virginica'

#print training confusion matrices
print("Training")
print("Manhattan Confusion Matrix Training")
confusion_matrix = pd.crosstab(X_train['class'], man_train['class'], rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n\n")

print("Euclidean Confusion Matrix Training")
confusion_matrix = pd.crosstab(X_train['class'], euc_train['class'], rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n\n")

print("Cosine Confusion Matrix Training")
confusion_matrix = pd.crosstab(X_train['class'], cos_train['class'], rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n\n")

#print testing confusion matrices
print("Testing")
print("Manhattan Confusion Matrix Training")
confusion_matrix = pd.crosstab(X_test['class'], man_test['class'], rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n\n")

print("Euclidean Confusion Matrix Training")
confusion_matrix = pd.crosstab(X_test['class'], euc_test['class'], rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n\n")

print("Cosine Confusion Matrix Training")
confusion_matrix = pd.crosstab(X_test['class'], cos_test['class'], rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)
print("\n\n")