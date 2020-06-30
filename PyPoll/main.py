import os
import csv

#list to hold just the votes
all_votes = []
#variables to hold the counts of each candidates votes
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0

csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    header = next(csvreader)
    
    if header != None:
        for row in csvreader:
            
            #sanity check
            #print(row)
            
            #creating a list with all the votes amounts
            all_votes.append(row[2])
            
            #sanity check
            #print(row[2])
        
        #storing the total number of votes
        total_votes = len(all_votes)
        
        #sanity check
        #print(total_votes)
    
    #iterating through to count the votes once
    for item in all_votes:
    
        #conditional to count khan's votes
        if item == "Khan":
            Khan_votes = Khan_votes + 1
            
        #conditional to count Correy's votes
        elif item == "Correy":
            Correy_votes = Correy_votes + 1
        
        #conditional to count Li's votes
        elif item == "Li":
            Li_votes = Li_votes + 1
        
        #conditional to count OTooley's votes
        elif item == "O'Tooley":
            OTooley_votes = OTooley_votes + 1
            
    #calculating the percentages for each candidates votes
    Khan_percent = (Khan_votes / total_votes) * 100
    
    Correy_percent = (Correy_votes / total_votes) * 100
    
    Li_percent =  (Li_votes / total_votes) * 100
    
    OTooley_percent =  (OTooley_votes / total_votes) * 100
    
    #rounding check
    Khan_percent = round(Khan_percent, 3)
    Correy_percent = round(Correy_percent, 3)
    Li_percent = round(Li_percent, 3)
    OTooley_percent = round(OTooley_percent, 3)
    
    #sanity check
    #print(Khan_percent)
    #print(Correy_percent)
    #print(Li_percent)
    #print(OTooley_percent)
