# -*- coding: utf-8 -*-
"""B21BB027.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LkZwsE5zc9mUZ_Lkz-KP19VVgab4nldj

Q1: A CSV file has been provided to you at this link. The given dataset is related to superstore
products and contains 21 columns. In the given dataset, “Sales” is the target variable (i.e., the
output).

i) Load the CSV data with the help of pandas and report the information regarding column
labels, column data types, memory usage, the number of non-null values in each column and statistical details like mean, count, and standard deviation.

ii) Find out the numerical and categorical features from the data.
"""

import pandas as pd
import numpy as np
import statistics as st
data = pd.read_csv('/content/Superstore.csv', encoding="windows-1252")
#print(data)
count=0
print(data.columns)
print('\n')
print(data.info())
print('\n')
print(data.mean())
print('\n')
print(data.count())
print('\n')
print(data.std())
print('\n')
print(data.notnull())

"""Q2: With the help of NumPy operations, solve the following questions.

i) Create an array of random floats with a range starting from 0 to 2.

ii) Show the standard deviation and mean of the above-generated data.
"""

import numpy as np
a = np.random.uniform(low=0,high=2,size=(20)) #random matrix
print(a)
print(a.mean()) #mean of a
print(a.std()) #standard deviationn of a

"""Q2 iii) Generate a random matrix of size (3,3) and find out the determinant, inverse, eigen values,
and eigen vectors of that.
"""

import numpy as np
a = np.random.uniform(low=0,high=2,size=(3,3))
print(a) #random matrix
print('\n')
print(np.linalg.det(a)) #determinant
print('\n')
print(np.linalg.inv(a)) #inverse
print('\n')
w, v = np.linalg.eig(a)
print(w) #eigen value
print('\n')
print(v) #eigen vector