# Project-2019
# Program and Scripting Project 2019 Fisher's Iris Data

## Introduction

The Iris flower data is a multivariate dataset introduced by biologist and statistician Ronald Fisher in 1936 in his paper *The use of multiple measurements in taxonomic problems."* It is an excellent example of linear discrimniant. This is based on the concept of searching for a linear combination of variables that best seperates two classes.[1]

## About the Iris Dataset

The dataset consists of fifty samples from three species of iris (*Iris setosa, Iris virginica* and *Iris versicolor*). 

![iris species](https://cdn-images-1.medium.com/max/1600/1*2uGt_aWJoBjqF2qTzRc2JQ.jpeg)


- The iris dataset contains the following data
  - 50 samples of the 3 different species of iris (150 samples in total)
  - Measurements: sepal lenght, sepal width, petal length and petal width.
- The format for the data: (sepal lenght, sepal width, petal lenght, petal width)[2]

![iris](https://raw.githubusercontent.com/ritchieng/machine-learning-dataschool/master/images/03_iris.png)


## Task



## Getting started
1. Download and install Python and Anaconda
2. All files associated with this project are available at https://github.com/NiamhOL/Project-2019
3. The Iris Dateset is saved as a .csv file in the associated Git Hub repository.

## Packages used in this project

The following packages were used to run statistical analysis and draw grpahs for this project.
- **_Python_** https://www.python.org/downloads/ - 
- **_Anaconda_** https://www.anaconda.com/distribution/
- **_iPython_** https://ipython.org/
- **_Pandas_** https://pandas.pydata.org/
- **_Scripy_** https://pypi.org/project/Scripy/
- **_Numpy_** http://www.numpy.org/
- **_Matplotlib_** https://matplotlib.org/
- **_Seaborn_** https://seaborn.pydata.org/

## Importing packages

The above packages can be imported into Python. Use **_Import_** function in **iPython** as follows:
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
from scripy import stats

## Importing the data

Import the iris.csv file using panda and examine the first few lines of data and the headings. 

data = pd.read_csv("iris.csv")

 data.head()

   Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
0   1            5.1           3.5            1.4           0.2  Iris-setosa
1   2            4.9           3.0            1.4           0.2  Iris-setosa
2   3            4.7           3.2            1.3           0.2  Iris-setosa
3   4            4.6           3.1            1.5           0.2  Iris-setosa
4   5            5.0           3.6            1.4           0.2  Iris-setosa

## Using Python for statistical analysis of the dataset

### Summary of basic statistics



data.describe()

               Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
count  150.000000     150.000000    150.000000     150.000000    150.000000
mean    75.500000       5.843333      3.054000       3.758667      1.198667
std     43.445368       0.828066      0.433594       1.764420      0.763161
min      1.000000       4.300000      2.000000       1.000000      0.100000
25%     38.250000       5.100000      2.800000       1.600000      0.300000
50%     75.500000       5.800000      3.000000       4.350000      1.300000
75%    112.750000       6.400000      3.300000       5.100000      1.800000
max    150.000000       7.900000      4.400000       6.900000      2.500000

data.corr()

                     Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
Id             1.000000       0.716676     -0.397729       0.882747      0.899759
SepalLengthCm  0.716676       1.000000     -0.109369       0.871754      0.817954
SepalWidthCm  -0.397729      -0.109369      1.000000      -0.420516     -0.356544
PetalLengthCm  0.882747       0.871754     -0.420516       1.000000      0.962757
PetalWidthCm   0.899759       0.817954     -0.356544       0.962757      1.00000

### Visualisation of statistics

## Summary 

## References

[1] Ogubdowole, O.O (Oct 31, 2017), _Basic analysis of the Iris Data set using python_ https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
[2] Hg, R. (2019) _Iris Dataset_ https://www,ritchieng.com/machine-learning-iris-dataset/#2


## Biblography 

10 minutes to pandas - https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

Machine Learning with Iris Dataset - https://kaggle.com/jchen2186/machine-learning-with-iris-dataset

Sir Ronald Alymer Fisher (Encyclopaedia Britannica) - https://www.britannica.com/biography/Ronald-Aylmer-Fisher

Fisher, R.A. (1936), _The Use of Multiple MEasuerments in Taxonomic Problems_, Annals of Eugenics, pp.179-188.

## Author - Niamh O'Leary

## Licence 
