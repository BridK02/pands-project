# Analysis of Fisher’s Iris data set
# Author Brid Kennedy

#dataset downloaded from http://archive.ics.uci.edu/ml/datasets/Iris and saved in my PANDS-PROJECT folder as iris.csv
#first thing to is test that I can manipulate the data as a csv file

import csv

#filename = "iris.csv"

#with open(filename, "rt") as csvFile:
   #csvReader = csv.reader(csvFile, delimiter=",")
   #for line in csvReader:
   #print (line[2]) #that works

csv_file = "iris.csv"
txt_file = "Iris.txt"
text_list = []

with open(csv_file, "r") as my_input_file:
    for line in my_input_file:
        line = line.split(",", 5) #This CSV file contains five 
        #fields: sepallength sepalwidth petallength,petalwidth,class which are delimited by commas. 
        text_list.append(" ".join(line))

'''with open(txt_file, "w") as my_output_file:
    my_output_file.write("#1\n")
    my_output_file.write("double({},{})\n".format(len(text_list), 5))
    for line in text_list:
        my_output_file.write("  " + line)
    print('File Successfully written.')'''

#The above has created a text file that has removed the commas

#All resources seem to point to pandas to group or summarise the variables. 
# I take the variables to mean sepal length, width etc
    


#because I am working with tabular data in Python I will use (import) the Python Data Analysis Library  
#ref https://datacarpentry.org/python-ecology-lesson/02-starting-with-data/
import pandas as pd
import seaborn as sns #data visualisation library
import matplotlib.pyplot as plt # allow me to plot the data
import numpy as np
#creating a dataframe of the iris csv
iris_df=pd.read_csv("iris.csv")
'''#testing how the iris_
#df looks
print (iris_df)
print (iris_df.dtypes) #summary of the data types to see if anything in the iris_df needs to be cleaned up
#the iris_
#df.dtypes above shows that the class is of type objects'''
'''iris_df.info() #this info shows that there are no null values and that the data again the the length and width 
#values are numerical whereas the class value are categorical

print (iris_df.sepallength)
print (iris_df.sepalwidth)
print (iris_df.petallength)
print (iris_df.petalwidth)
print (iris_df['class'])# finding the right syntax to get around class was a half hour I won't get back in my life

meanValues= iris_df.groupby('class').mean() #find the means of the four measurements using the groupby  function on class 
maxValues= iris_df.groupby('class').max()
minValues= iris_df.groupby('class').min()


print(meanValues)
print(maxValues)
print(minValues)

#iris_df.plot.scatter(x='class',y = 'sepallength')
ax = iris_df.plot.scatter(x="class", y="sepallength", color="DarkBlue", label="sepallength")
iris_df.plot.scatter(x="class", y="sepalwidth", color="DarkGreen", label="sepalwidth", ax=ax);
iris_df.plot.scatter(x="class", y="petallength", color="DarkRed", label="petallength", ax=ax);
iris_df.plot.scatter(x="class", y="petalwidth", color="Yellow", label="petalwidth", ax=ax);

plt.savefig('scatterplot.png')

plt.show()'''

#iris_df.plot(kind ='scatter', x ='sepallength', y ='sepalwidth')

sns.set_style('whitegrid') #using seaborn to distinguish between the 3 classes https://medium.com/@Ansh_Patel/deep-dive-eda-on-iris-dataset-e8b04faf2bf7
sns.FacetGrid(iris_df, hue = 'class', height = 5)\
.map(sns.scatterplot, 'sepallength', 'sepalwidth')\
.add_legend()
plt.savefig('Figure 1 Sepal characteristic colour coded 2D scatter plot.png')
#the colour coding of this plot shows good separation of iris's of the 
#setosa class based on sepal characteristic in comaprison to versicolour and virginica,
#this indicates that these two classes of Iris can be classified based on the two sepal measurements
sns.set_style('whitegrid')
sns.pairplot(iris_df, hue = 'class')
plt.savefig('Figure 2 Bivariate analysis.png')
#the bivariate analysis really shows the large overlap between versicolour and virginica when it comes to sepal length and width 
#however there is significantly better seperation of these two classes using the petal length and width however there remains some overlap

fig, axes = plt.subplots(2, 2, figsize = (14, 9))
sns.boxplot(data = iris_df, x = 'class', y = 'petallength',ax = axes[0,0])
sns.boxplot(data = iris_df, x = 'class', y = 'petalwidth',
ax = axes[0,1])
sns.boxplot(data = iris_df, x = 'class', y = 'sepallength',
ax = axes[1,0])
sns.boxplot(data = iris_df, x = 'class', y = 'sepalwidth',
ax = axes[1,1])
plt.savefig('Figure 3 Box plots.png')