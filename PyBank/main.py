import os
import csv
import statistics

#List to hold the Profit/Loss column
Profit_Losses = []
#New list with the types changed to integers
New_Profit_Losses = []
#List to hold to the Months
Month_Year = []


csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    header = next(csvreader)


    if header != None:
        for row in csvreader:
            
            #creating a list with all the profit/loss amounts
            Profit_Losses.append(row[1])
            #creating a list with all the months
            Month_Year.append(row[0])
            
    #Check to see I collected the data correctly
    #print(Profit_Losses)
    #print(Month_Year)
    
    #loop to convert the list items into integers
    for item in Profit_Losses:
        
        New_Profit_Losses.append(int(item))
        
    #sanity check
    #print(New_Profit_Losses)
    
    total_months = len(Month_Year)
    
    net_total = sum(New_Profit_Losses)

    mean = statistics.mean(New_Profit_Losses)
    #round to the second decimal place
    new_mean = round(mean, 2)
    
    greatest_increase = max(New_Profit_Losses)
    
    greatest_decrease = min(New_Profit_Losses)
    
    increase_index = New_Profit_Losses.index(max(New_Profit_Losses))
    
    decrease_index = New_Profit_Losses.index(min(New_Profit_Losses))
    
    
    #sanity check
    #print(increase_index)
    #print(New_Profit_Losses[increase_index])
    
print("Financial Analysis")
print("----------------------------------------------")
print(f'Total months: {total_months}')
print(f'Total: ${net_total}')
print(f'Average Change: ${new_mean}')
print(f'Greatest increase in profits: {Month_Year[increase_index]} (${greatest_increase})')
print(f'Greatest decrease in profits: {Month_Year[decrease_index]} (${greatest_decrease})')

file_path = "Analysis/Analysis.txt"

file = open(file_path, "w")
file.write('Financial Analysis\n')
file.write('-----------------------------------------------\n')
file.write(f'Total months: {total_months}\n')
file.write(f'Total: ${net_total}\n')
file.write(f'Average Change: ${new_mean}\n')
file.write(f'Greatest increase in profits: {Month_Year[increase_index]} (${greatest_increase})\n')
file.write(f'Greatest decrease in profits: {Month_Year[decrease_index]} (${greatest_decrease})\n')
file.close()
