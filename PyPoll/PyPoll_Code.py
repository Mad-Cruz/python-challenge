# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 19:59:54 2023

@author: MadSa
"""
import os
cwd = os.getcwd()
# print(cwd)
import csv
F = "Resources/election_data.csv"

count1 = 0 #total votes has a value of 0 to start the for loop
count2 = 0
count3 = 0
candidate_votes = [] #creates empty list
candidate_vote_percentage = []
winning_candidate = ""
winning_votes = 0
specific_candidates = []


#reading the data from the csv file
with open(F,"r") as Election_Data_Readable:
    Election_Data_Being_Read = csv.reader(Election_Data_Readable)
    
    #skips the header
    next(Election_Data_Being_Read)
    
    #for loop that reads every row in the file
    for row in Election_Data_Being_Read:
      
        if row[2] not in specific_candidates:
            specific_candidates.append(row[2])

        if row[2] == specific_candidates[0]:
            count1 += 1
   
        elif row[2] == specific_candidates[1]:
            count2 += 1
            
        elif row[2] == specific_candidates[2]:
            count3 += 1
            
    candidate_votes.append(count1)        
    candidate_votes.append(count2)
    candidate_votes.append(count3)
    
total_votes = int(sum(candidate_votes))

#round,5 formats the below to 5 decimal points
percentage_Charles = round(int(candidate_votes[0])/total_votes,5)
percentage_Diana = round(int(candidate_votes[1])/total_votes,5)
percentage_Raymon = round(int(candidate_votes[2])/total_votes ,5)

#"{:.3%}".format() converts the decimal to a percentage - .3 means 3 digits after the decimal
candidate_vote_percentage.append("{:.3%}".format(percentage_Charles))
candidate_vote_percentage.append("{:.3%}".format(percentage_Diana))
candidate_vote_percentage.append("{:.3%}".format(percentage_Raymon))


#print(total_votes) 
#print(specific_candidates)
#print(candidate_vote_percentage)      
#print(candidate_votes)

max_votes_index = candidate_votes.index(max(candidate_votes))
#print(max_votes_index)


# creates the file, allows the file to be written, then actually writes the file
D = "Analysis/PyPoll Analysis.txt"    
with open(D, "w") as Election_Data_Write:
    Election_Data_Write.write("Election Results\n")
    Election_Data_Write.write("----------------------------------------\n")
    Election_Data_Write.write(f"Total Votes: {total_votes}\n")
    Election_Data_Write.write("----------------------------------------\n")
    Election_Data_Write.write(f"{specific_candidates[0]}: {candidate_vote_percentage[0]} {candidate_votes[0]}\n")
    Election_Data_Write.write(f"{specific_candidates[1]}: {candidate_vote_percentage[1]} {candidate_votes[1]}\n")
    Election_Data_Write.write(f"{specific_candidates[2]}: {candidate_vote_percentage[2]} {candidate_votes[2]}\n")
    Election_Data_Write.write("----------------------------------------\n")
    Election_Data_Write.write(f"Winner: {specific_candidates[max_votes_index]}\n")
            
