#@name perceptron.py
#@author Aedan Wells
#@class Machine Learning
#@date 10/11/2022
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

#performs the perceptron algorithm and prints the perceptron equation
#param iris is the dataset of 2 species this is performed on
def perceptron(iris):
    #init constanst
    change = 1
    w_petal_len = 1
    w_petal_wid = 1
    w_sepal_len = 1
    w_sepal_wid = 1
    bias = 0
    move_num = 0
    #until there is no change OR we reach 200 line moves
    while change != 0 and move_num <= 200:
        change = 0
        #for each flower
        for index, flower in iris.iterrows():
            #grab the a value from adding all values and weights
            a = w_petal_len*flower['petallength'] + w_petal_wid*flower['petalwidth'] + w_sepal_len*flower['sepallength'] + w_sepal_wid*flower['sepalwidth'] + bias
            #if a*class is <= 0, reset weights based on the missing value
            if a*flower['class'] <= 0:
                w_petal_len = w_petal_len + (flower['class']*flower['petallength'])
                w_petal_wid = w_petal_wid + (flower['class']*flower['petalwidth'])
                w_sepal_len = w_sepal_len + (flower['class']*flower['sepallength'])
                w_sepal_wid = w_sepal_wid + (flower['class']*flower['sepalwidth'])
                bias = bias + flower['class']
                change = 1
                move_num = move_num + 1
    #print equation
    print(str(w_petal_len) + "*petallength + " + str(w_petal_wid) + "*petalwidth + " + str(w_sepal_len) + "*sepallength +" + str(w_sepal_wid) + "*sepalwdith + " + str(bias) + " = 0")
            

#read csv
iris = pd.read_csv('iris_csv.csv')

#take out virginica, find perceptron of remaining
iris_set_versi = iris.loc[iris['class'] != "Iris-virginica"]
print("Species: Setosa v Versicolor:")
iris_set_versi.replace("Iris-versicolor", -1, inplace=True)
iris_set_versi.replace("Iris-setosa", 1, inplace=True)
perceptron(iris_set_versi)
print("\n")

#take out versicolor, find perceptron of remaining
iris_set_virgin = iris.loc[iris['class'] != "Iris-versicolor"]
print("Species: Setosa v Virginica:")
iris_set_virgin.replace("Iris-virginica", -1, inplace=True)
iris_set_virgin.replace("Iris-setosa", 1, inplace=True)
perceptron(iris_set_virgin)
print("\n")

#take out setosa, find perceptron of remaining
iris_virgin_versi = iris.loc[iris['class'] != "Iris-setosa"]
print("Species: Virginica v Versicolor:")
iris_virgin_versi.replace("Iris-versicolor", -1, inplace=True)
iris_virgin_versi.replace("Iris-virginica", 1, inplace=True)
perceptron(iris_virgin_versi)


