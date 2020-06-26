import os
import csv

#List to hole the Profit/Loss column
Profit_Losses = []

csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    header = next(csvreader)

    if header != None:
        for row in csvreader:
            Profit_Losses.append[row(1)]
