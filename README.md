# Project-2019
# Program and Scripting Project 2019 Fisher's Iris Data

# Course: Higher Diploma in Data Analytics
# Module: Programming and Scripting
# Year & Semester: 2019 - 01
# Student: Niamh O'Leary
# ID: G00376339

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

The aim of this project is to give an overview of Fisher's Iris Dataset, by using Python programming lanuage for statistical analysis. 


## Getting started
1. Download and install Python and Anaconda
2. All files associated with this project are available at https://github.com/NiamhOL/Project-2019
3. The Iris Dateset is saved as a .csv file in the associated Git Hub repository.

## Packages used in this project

The following packages were used to run statistical analysis and draw grpahs for this project.
- **_Python_** https://www.python.org/downloads/ 
- **_Anaconda_** https://www.anaconda.com/distribution/ - is the easiest way to perfrom Python data science machine learning on Linux, Windows and Mac OS. 
- **_iPython_** https://ipython.org/ - it an interactive command-line terminal for Python.
- **_Pandas_** https://pandas.pydata.org/ - pandas is an "open source, BSD-licensed library providing high-perfromance, easy-to-use data structures and data analysis tool."[3] 
- **_Scripy_** https://pypi.org/project/Scripy/ - which allows the user to run system commands in the same shell through it's main tool *shell.Run().
- **_Numpy_** http://www.numpy.org/ - is the fundamental package for scientific computing within Python.
- **_Matplotlib_** https://matplotlib.org/ - is a 2D plotting library within Python within which the user can generate a wide variety of figures, including plots, histograms, scetterplots etc.
- **_Seaborn_** https://seaborn.pydata.org/ - is a Python data visualisation library based on matplotlib. It provides a high level interface for drawing infromative statistical graphs. 

## Importing packages

The above packages can be imported into Python. Use **_Import_** function in **iPython** as follows:
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
from scripy import stats

## Importing the data

Import the iris.csv file using panda and examine the first few lines of data and the headings. 



## Using Python for statistical analysis of the dataset

### Summary of basic statistics 

The fist step in anlysisng the Iris Dataset is to take a closer look at the data. There are five columns in this dataset with the following variable names: Sepal Lenght, Sepal Width, Petal Length, Petal Width and Species. The first four variables are meaurements in centimeters and the fith vairiable is the name of the species. All the species were sampled from the same location the Gaspe Peninsula and measured bu the same person Edger Anderson. 

##### i. Overview of the data

When analysing a dataset it is important to firstly gain an understanding of the dataset. By using the *group.by* function one is able to see how many samples were available for each species.

![Summary](https://github.com/NiamhOL/Project-2019/blob/master/Iris%20Species%20Overview.PNG)

![Overview](https://github.com/NiamhOL/Project-2019/blob/master/Iris%20data%20overview%202.PNG)

![Overview1](https://github.com/NiamhOL/Project-2019/blob/master/Iris%20data%20overview%20start.PNG)

![Sample](https://github.com/NiamhOL/Project-2019/blob/master/iris%20overview%20sample.PNG)

By using head, tail and sample functions is it possible to get a general overiew of the datset at different levels. This allows for a great understanding of the data anvailable for analysis. Using the*sample* function generates a random sample of the data within the database. From this one can see that 'Iris-setosa' appears to have a smaller petal compared to the other species. Therefore, even without detailed stastical analysis, there are already signs of compariability between 'Iris-virginica' and 'Iris-versicolor'.

#### ii. Summary of the dataset

Using the *describe* function in pandas generates an output table with a statistical overview of the data. 

![Basic](https://github.com/NiamhOL/Project-2019/blob/master/Iris%20dataset%20description.PNG)








### Visualisation of statistics


#### Boxplot

The best tool to identify the outliers is the boxplot. "Through the box plots, we find the minimum, lower quartile (25th percentile), median (50th percentile), upper quartile (75th percentile), and a maximum of a contunues variable."[] A boxplot of the Iris Dataset can 


![Boxplot2](https://github.com/NiamhOL/Project-2019/blob/master/Plot%20showing%20data%20points%20on%20top%20of%20boxplot.png)


![Boxplot](https://github.com/NiamhOL/Project-2019/blob/master/Boxplot%20by%20Species.png)


The box plot shows the univariate form of each meaurement. 

#### Histogram

![Histogram](https://github.com/NiamhOL/Project-2019/blob/master/Histogram.png)

#### Relationships



![Relationahip](https://github.com/NiamhOL/Project-2019/blob/master/Relationships%20between%20species.png)

Scatterplots can be helpful to spot structured relationships between differnt variables. 





#### Violin Plot

![violin](https://github.com/NiamhOL/Project-2019/blob/master/Violin%20plot%20Petal%20Length.png)

#### Hexagonal Plot
![Hex](https://github.com/NiamhOL/Project-2019/blob/master/Hexagonal%20Bin%20Plot%20Sepal%20Length%20Sepal%20Width.png)


#### Correlations 

![Correlation](https://github.com/NiamhOL/Project-2019/blob/master/Correlation%20matrix.png)





## Summary 

## References

[1] Ogubdowole, O.O (Oct 31, 2017), _Basic analysis of the Iris Data set using python_ https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
[2] Hg, R. (2019) _Iris Dataset_ https://www,ritchieng.com/machine-learning-iris-dataset/#2
[3] httpS://pandas.pydata.org
[] https://datascienceplus.com


## Biblography 

10 minutes to pandas - https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

Machine Learning with Iris Dataset - https://kaggle.com/jchen2186/machine-learning-with-iris-dataset

Sir Ronald Alymer Fisher (Encyclopaedia Britannica) - https://www.britannica.com/biography/Ronald-Aylmer-Fisher

Fisher, R.A. (1936), _The Use of Multiple MEasuerments in Taxonomic Problems_, Annals of Eugenics, pp.179-188.

https://www.kaggle.com/xuhewen/iris-dataset-visualization-and-machine-learning

https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis.com

https://www.kaggle.com/ekapylski/iris-dataset-visualization

https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation


## Author - Niamh O'Leary

## Licence 
