# Iris Dataset Analysis #

# Begin by importing pandas, seaborn, a data analysis toolkit and graphing library #

import pandas as pd     
import seaborn as sns  
import matplotlib.pyplot as plt  
sns.set(style="white", color_codes=True)

# To import the Iris Dataset: #

iris = pd.read_csv('Iris.csv')

# to view the data # 

iris.head()

# Generate a sample from each species #      

iris['Species'].value_counts()

# Overview of Species Distribution from the  start #

print(iris.head()) 

# Overview of Species Distribution from the end #

print(iris.tail()) 

# To generate a Scatterplot using pandas #

iris.plot(kind="scatter" , x="SepalLenghtCm" , y="SepalWidthCm")

# To display the plot #

plt.show()

# To change colours and size & display plot #

iris.plot(kind="scatter" , x="SepalLenghtCm" , y="SepalWidthCm" , color="green" , s=70)
plt.show()

# To generate a jointplot using seaborn - joing a bivariate scatterplot and a univariate histogram in one grapph #

sns.joint(x="SepalLenghtCm" , y="SepalWidthCm" , data=iris , size=5)
plt.show()

# To generate a Boxplot of Petal Length #

sns.boxplot(x="Species" , y="PetalLenghtCm" , data=iris)
plt.show()

# To generate a striplot and add datapoints on top of the Boxplot #

ax= sns.boxplot(x="Species" , y="PetalLengthCm", data=iris)
    ...: ax= sns.stripplot(x="Species" , y="PetalLengthCm", data=iris, jitter=True, e
    ...: dgecolor="gray")

In [13]: plt.show()

# To generate a violin plot #

sns.violinplot(x="Species" , y="PetalLengthCm" , data=iris, size=7)

# Using pairplot to analyse the relationship between species for all characteristic combinations #


sns.pairplot(iris.drop("Id", axis=1), hue="Species", height=3)

# Plot showing kernal desnity estimation #

sns.pairplot(iris.drop("Id", axis=1, hue="Species", size=3, diag_kind="kde")

# To generate a Hexagonal bin plot #

sns.jointplot(x="SepalLengthCm", y="SepalWidthCm", data=iris, size=10, ratio=10, kind='hex' , color='purple')

# Boxplot by speciies #

iris.drop("Id", axis=1) .boxplot(by="Species" , figsize=(10, 10))

# Correlation Matrix #              https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis.com

 plt.figure(figsize=(10, 8))
    ...: sns.heatmap(corr,
    ...:             xticklabels=corr.columns.values,
    ...:             yticklabels=corr.columns.values,
    ...:            cmap='viridis' , annot=True)

# Generating an Andrews Plot #

 def get_red_blue_green_cmap():
    ...:     custom_rgb = ["#4c72B0" , "#55A868" , "#C44E52"];
    ...:     custom_cmap = mpl.colors.ListedColormap(custom_rgb)
    ...:     return custom_cmap
    ...:

In [41]: from pandas.tools.plotting import andrews_curves

In [42]: andrews_curves(iris.drop("Id" , axis=1), "Species" , colormap=get_red_blue_g
    ...: reen_cmap())