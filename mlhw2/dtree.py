#@name dtree.py
#@author Aedan Wells
#@class Machine Learning
#@date 10/11/2022
import pandas as pd
from sklearn import tree
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

#grab tic_tac_toe dataset
tic = pd.read_csv('tic-tac-toe.data', names=['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'Outlook'])
tic = tic.replace(to_replace='x', value=0)
tic = tic.replace(to_replace='o', value=1)
tic = tic.replace(to_replace='b', value=2)

x_num = tic.iloc[:,:-1]
tic.replace('negative',0,inplace=True)
tic.replace('positive',1,inplace=True)
y = tic.iloc[:,9].values


classifier = tree.DecisionTreeClassifier(criterion = 'entropy', random_state =  42)
classifier.fit(x_num,y)

plt.figure(figsize=(13, 13))
tree.plot_tree(classifier,filled=True, class_names=True)

plt.show()
