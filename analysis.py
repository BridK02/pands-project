# Analysis of Fisher’s Iris data set
# Author Brid Kennedy


#first thing to is test that I can manipulate the data as a csv file

import csv

#filename = "iris.csv"

#with open(filename, "rt") as csvFile:
   # csvReader = csv.reader(csvFile, delimiter=",")
   # for line in csvReader:
   #  print (line[2]) #that works

#because I am working with tabular data in Python I will use (import) the Python Data Analysis Library  
#ref https://datacarpentry.org/python-ecology-lesson/02-starting-with-data/
import pandas as pd
#creating a dataframe of the iris csv
iris_df=pd.read_csv("iris.csv")
#testing how the df looks
#print (iris_df)

print (iris_df.columns)


