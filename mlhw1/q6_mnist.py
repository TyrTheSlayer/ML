from math import sqrt
import pandas as pd
import numpy as np
from numpy.linalg import norm
import gzip
import sys; 
import pickle;
from matplotlib import pyplot
import numpy_indexed as npi

#add the mnist dataset
f = gzip.open('mnist.pkl.gz', 'rb')
if sys.version_info < (3,):
    data = pickle.load(f)
else:
    data = pickle.load(f, encoding='bytes')
f.close()
(x_train, y_train), (x_test, y_test) = data

#generate average datapoints (provided by numpy)
digits, means = npi.group_by(y_train).mean(x_train)

man_train = np.zeros(60000, dtype = int)
man_test = np.zeros(10000, dtype = int)
euc_train = np.zeros(60000, dtype = int)
euc_test = np.zeros(10000, dtype = int)
cos_train = np.zeros(60000, dtype = int)
cos_test = np.zeros(10000, dtype = int)
man_avg = np.zeros(10, dtype=int)

#find distances
for i in x_train.size:
  #manhattan
  