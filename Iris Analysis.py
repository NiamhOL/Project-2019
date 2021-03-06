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

# Scatterplot in Seaborn #

iris = sns.load_dataset('iris')
sns.lmplot( x="petal_length" , y="petal_width" , data=iris, fit_reg=False, hue='species' , legend=False)
plt.legend(loc='lower right')
sns.plt.show()


# To display the plot #

plt.show()

# To change colours and size & display plot #

iris.plot(kind="scatter" , x="SepalLenghtCm" , y="SepalWidthCm" , color="green" , s=70)
plt.show()

# To generate a jointplot using seaborn - joing a bivariate scatterplot and a univariate histogram in one grapph #

sns.joint(x="SepalLenghtCm" , y="SepalWidthCm" , data=iris , size=5)
plt.show()

# To generate a Boxplot  #

sns.boxplot(x="Species" , y="PetalLengthCm" , data=iris)
plt.show()

sns.boxplot(x="Species" , y="SepalLengthCm" , data=iris)
plt.show()

sns.boxplot(x="Species" , y="PetalWidthCm" , data=iris)
plt.show()

sns.boxplot(x="Species" , y="SepalWidthCm" , data=iris)
plt.show()

# To generate a striplot and add datapoints on top of the Boxplot #

ax= sns.boxplot(x="Species" , y="PetalLengthCm", data=iris)
    ...: ax= sns.stripplot(x="Species" , y="PetalLengthCm", data=iris, jitter=True, e
    ...: dgecolor="gray")

In [13]: plt.show()

# To generate a violin plot #

sns.violinplot(x="Species" , y="PetalLengthCm" , data=iris, size=7)

sns.violinplot(x="Species" , y="PetalWidthCm" , data=iris, size=7)

sns.violinplot(x="Species", y="SepalLengthCm" , data=iris, size=7)

sns.violinplot(x="Species", y="SepalWidthCm" , data=iris, size=7)

# Using pairplot to analyse the relationship between species for all characteristic combinations #


sns.pairplot(iris.drop("Id", axis=1), hue="Species", height=3))

# Plot showing kernal desnity estimation #

sns.pairplot(iris.drop("Id", axis=1, hue="Species", size=3, diag_kind="kde")

# To generate a Hexagonal bin plot #

sns.jointplot(x="SepalLengthCm", y="SepalWidthCm", data=iris, size=10, ratio=10, kind='hex' , color='purple')

sns.jointplot(x="PetalLengthCm", y="PetalWidthCm", data=iris, size=10, ratio=10, kind='hex' , color='orange')

# Boxplot by speciies #

 sns.boxplot(by="Species" , figsize=(10, 10))

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
    ...:     return cuythonstom_cmap
    ...:

from pandas.tools.plotting import andrews_curves

 andrews_curves(iris.drop("Id" , axis=1), "Species" , colormap=get_red_blue_g
    ...: reen_cmap())

# Generating a Radviz plot #
   from pandas.tools.plotting import radviz

# Histograms #

 iris_long = pd.melt(iris, "Species" , var_name="measurement")

 g = sns.FacetGrid(iris_long, hue="Species" , col="measurement" , col_wrap=2, sharex=False)

 g.map(plt.hist, "value", alpha=.4)
 <seaborn.axisgrid.FacetGrid at 0x1fc0de7dc18>

 plt.show()

 # Histogram with addition plot #

 sns.distplot(a=iris['PetalWidthCm'], bins=40, color='m')

 # Histogram of all three species with colour change #

 for feature in range(iris.data.shape[1]):
    ...:     plt.subplot(2, 2, feature+1)
    ...:     for label, color in zip(range(len(iris.target_names)), colors):
    ...:         plt.hist(iris.data[iris.target==label, feature],
    ...:         label=iris.target_names[label],
        ...:         color=color)
    ...:     plt.xlabel(iris.feature_names[feature])
    ...:     plt.legend()

# Facet Plots #

iris = iris.map(sns.kdeplot, 'SepalLengthCm')