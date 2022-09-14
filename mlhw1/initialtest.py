import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

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

print(df.size)