import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #check to see if it's printing the right thing
    #for row in csvreader:
        #print(row)
