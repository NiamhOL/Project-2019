# Ovreview of Iris dataset and basic statistics 

import pandas as import pdb; pdb.set_trace()

import numpy as numpy

import matplotlib.pyplot as pyplot

data = pd.read_csv("iris.csv")

data.head()

Out[5]:
   Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
0   1            5.1           3.5            1.4           0.2  Iris-setosa
1   2            4.9           3.0            1.4           0.2  Iris-setosa
2   3            4.7           3.2            1.3           0.2  Iris-setosa
3   4            4.6           3.1            1.5           0.2  Iris-setosa
4   5            5.0           3.6            1.4           0.2  Iris-setosa

In [7]: data.describe()
Out[7]:
               Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
count  150.000000     150.000000    150.000000     150.000000    150.000000
mean    75.500000       5.843333      3.054000       3.758667      1.198667
std     43.445368       0.828066      0.433594       1.764420      0.763161
min      1.000000       4.300000      2.000000       1.000000      0.100000
25%     38.250000       5.100000      2.800000       1.600000      0.300000
50%     75.500000       5.800000      3.000000       4.350000      1.300000
75%    112.750000       6.400000      3.300000       5.100000      1.800000
max    150.000000       7.900000      4.400000       6.900000      2.500000


In [10]: data.corr()
Out[10]:
                     Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
Id             1.000000       0.716676     -0.397729       0.882747      0.899759
SepalLengthCm  0.716676       1.000000     -0.109369       0.871754      0.817954
SepalWidthCm  -0.397729      -0.109369      1.000000      -0.420516     -0.356544
PetalLengthCm  0.882747       0.871754     -0.420516       1.000000      0.962757
PetalWidthCm   0.899759       0.817954     -0.356544       0.962757      1.000000