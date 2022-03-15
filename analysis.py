# Analysis of Fisher’s Iris data set
# Author Brid Kennedy


#first thing to is test that I can manipulate the data as a csv file

import csv

filename = "iris.data"

with open(filename, "rt") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    for line in csvReader:
        print (line[2]) #that works