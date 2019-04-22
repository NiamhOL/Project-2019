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

Using the *describe* function in pandas generates an output table with a statistical overview of the data and gain an understanding of the mean, standard deviation, min, max and quartiles based on sepal-length, sepal-width, petal-length and petal-width. By analysing the mean, max and standard deviation a general overview of the four meaurements can be obtained. The standard deviation is used to tell hoe the numbers of a group are spread out from the average (the mean). Petal-length has the greatest standard deviation, indicating that the samples for this data point are most widely distributed. 

![Basic](https://github.com/NiamhOL/Project-2019/blob/master/Iris%20data%20discrip..PNG)


### Visualisation of statistics
*“Visualization may not be as precise as statistics, but it provides a unique view onto data that can make it much easier to discover interesting structures than numerical methods.”*[5] Statistics are used to describe and quantify dats. Visualisation is what enables the data to be seen. Alowing the reader see patterns, which assists in a greater understanding of the data.

There are many differnt ways of using Exploratory Data Analysis to analyse Fisher's Iris Data Set. I have outlines a variety of diferent methods in the project, deccribing what can be seen from the graphs/plots and docementing the positives and negatives of using these different visualisations. Please see the file *Iris Analysis.py* in the my GitHub Respository NiamhOL/Project-2019 for a detailed description of the python code used to generated the different graphs/plots. 


#### Boxplot

"The person widely attributed as being the father of visual methods is John W Tukey, the prominent statistician who pioneered Exploratory Data Analysis. He championed techniques for visually exploring data to unearth discoveries that are otherwise indiscernible in the original data form or potentially masked by the aggregating nature of some statistical treatments." [6]

The best tool to identify the outliers is the boxplot. Through the box plots, we find the minimum, lower quartile (25th percentile), median (50th percentile), upper quartile (75th percentile), and a maximum of a contunues variable.


![Boxplot2](https://github.com/NiamhOL/Project-2019/blob/master/Plot%20showing%20data%20points%20on%20top%20of%20boxplot.png)

I initially generated a simple Box Plot looking at PetalLenght for each species. TO gain a better understanding of the relevent data, I created an overlay of a Box Plot and Scatter Plot. This gave a better view of the outliers. 

TO make it eaier for the reader to analyse all three species, I created a multi Box Plot view of all three species by Petal Length, Petal Width, Sepal Length and Sepal Width. These box plots show the univariate form of each meaurement. 

![Boxplot](https://github.com/NiamhOL/Project-2019/blob/master/Boxplot%20by%20Species.png)

From these Box Plots it can be seen that Petal Length and Sepal Length have the greatest range and number of outliers, especially for "Iris-virginica".


#### Histograms

![Histogram](https://github.com/NiamhOL/Project-2019/blob/master/Histogram.png)

![Histogram3](https://github.com/NiamhOL/Project-2019/blob/master/Histogram%203%20species.png)

![Histogram3](https://github.com/NiamhOL/Project-2019/blob/master/Histogram%20with%20three%20species.png)

#### Scatterplots

Scatterplots are useful for identifying trends in statistial data. Each observation in a Scatter Plot has two co-ordiantes (X & Y). The "point" of observation is where thse two co-ordiantes intersect. Relationshps between sets of data can be observed depending on the shape of the points. If the data points show an "up-hill" pattern from left to right, then there is a positive relationship between X & Y. Conversely if the pattern is "downhill" there is a positive relationship between X & Y. If the dats is scattered then there is no relationship between the X & Y.

![Scatter](https://github.com/NiamhOL/Project-2019/blob/master/graph%20assigning%20eash%20species%20a%20colour.png)

This scatterplot Sepal Width v Sepal Lenght, shows a somewhat positive relationship for "Iris-setosa" but not as strong for the other two species.

![Relationahip](https://github.com/NiamhOL/Project-2019/blob/master/Relationships%20between%20species.png)

By creating a multigraph resperesntation of the data is is easy to see the differing relationships between the different data points. 

#### Violin Plot

![violin](https://github.com/NiamhOL/Project-2019/blob/master/Violin%20plot%20Petal%20Length.png)

#### Hexagonal Plot

A Hexagonal Plot is generated by covering the data range with a series of hexagons. The darker the colouring if the hexagone indicates a greater number of observations. 

![Hex](https://github.com/NiamhOL/Project-2019/blob/master/Hexagonal%20Bin%20Plot%20Sepal%20Length%20Sepal%20Width.png)

I generated a Hexagonal Plot to visualise Sepal Width with Sepal Length. The greatest number of observations occured in three areas of the plot - Sepal Width 3.5cm Sepal Lengthe 5.0cm, Sepal Width 3.0sm Sepal Length 5.5-6.0 and Sepal Width 3.0 & Sepal Length 6.5-7.0. 

To validate this plot I generated a Hexagonal and Histogram plot. 

#### Andrews Plot

Andrews Plot is a mutlivariate analysis. From the Andrews Plot of the Iris Data Set it is clear that one type of Iris is distinct from the other two but differentiating between the other two is not as easy. 

![Andrews](https://github.com/NiamhOL/Project-2019/blob/master/Andrews%20plot.png)

#### Radviz Analysis

A Radviz plot is another multivariate data visualisation. "In Radviz, each dimension in the dataset is represented by a dimensional anchor, and each dimensional anchor is distributed evenly on a unit circle. Each line in the data set corresponds to a point in the projection, that is linked to every dimensional anchor by a spring. Each spring’s stiffness corresponds to the value for that particular thing in that particular dimension. The position of the point is defined as the point in the 2D space where the spring’s tension is minimum."[6]

![Radviz](https://github.com/NiamhOL/Project-2019/blob/master/Radviz%20plot.png)


#### Correlations 

Corelation in statistcs is important as it repersents how stongly pairs of vaiables are realted. Often correalation is generted by stattitical packages such as SPSS. R etc. "Like all statistical techniques, correlation is only appropriate for certain kinds of data. Correlation works for quantifiable data in which numbers are meaningful, usually quantities of some sort. It cannot be used for purely categorical data, such as gender, brands purchased, or favorite color.2 [7] I wanted to generate a visualisation of the correlations(if any) with the Iris Data Set. Therefore I used the *heatmap* funtion to see which parameters best correlate with each other. According to the correlation matrix PetalLengthCm and PetalWidthCm have positive correlation. 

![Correlation](https://github.com/NiamhOL/Project-2019/blob/master/Correlation%20matrix.png)







## Summary 

## References

[1] Ogubdowole, O.O (Oct 31, 2017), _Basic analysis of the Iris Data set using python_ https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
[2] Hg, R. (2019) _Iris Dataset_ https://www,ritchieng.com/machine-learning-iris-dataset/#2
[3] httpS://pandas.pydata.org
[] https://datascienceplus.com
[5],[6] https://www.statisticsviews.com/details/feature/6314441/Visualising-Statistics-The-importance-of-seeing-not-just-describing-data.html
[6] https://cran.r-project.org/web/packages/Radviz/vignettes/single_cell_projections.html
[7] https://www.surveysystem.com/correlation.htm

## Biblography 

10 minutes to pandas - https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

Machine Learning with Iris Dataset - https://kaggle.com/jchen2186/machine-learning-with-iris-dataset

Sir Ronald Alymer Fisher (Encyclopaedia Britannica) - https://www.britannica.com/biography/Ronald-Aylmer-Fisher

Fisher, R.A. (1936), _The Use of Multiple MEasuerments in Taxonomic Problems_, Annals of Eugenics, pp.179-188.

https://www.kaggle.com/xuhewen/iris-dataset-visualization-and-machine-learning

https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis.com

https://www.kaggle.com/ekapylski/iris-dataset-visualization

https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation

http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.608.6250&rep=rep1&type=pdf

## Author - Niamh O'Leary

## Licence 
