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
        print(total_votes)
    
    #iterating through to count the votes once
    for item in all_votes:
    
        #conditional to count khan's votes
        if item == "Khan":
            
            Khan_votes = Khan_votes + 1
            
        #conditional to count Correy's votes
        
