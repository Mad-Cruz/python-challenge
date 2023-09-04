# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 21:59:26 2023

@author: MadSa
"""
import os
cwd = os.getcwd()
# print(cwd)
import csv
P = "Resources/budget_data.csv"
date = []
profit_and_loss = []
changes_in_PnL = []
total_number_of_months = 0
greatest_increase = ["", 0]
greatest_decrease = ["",0]


# reading the data from the csv file
with open(P,"r") as Budget_Data_Readable:
    Budget_Data_Being_Read = csv.reader(Budget_Data_Readable)
   
    # skips the header
    next(Budget_Data_Being_Read) 
   
    # for loop that reads every row in the file
    for row in Budget_Data_Being_Read:
       
        # append adds the info in column A to the date list, using the for loop to go one by one
        date.append(row[0])
        # int changes the info in column B to integers so that they can be added
        profit_and_loss.append(int(row[1]))
        monthly_profit_and_loss = int(row[1])
        # counts the number of months by adding 1 every time it goes through the for loop
        # += is the same as saying total = total + 1
        total_number_of_months += 1
        # changes in PnL is calculated by subtracting the previous month from the current month
        # because there's no  previous month before Jan, we need to start with Feb
        # the below stores the changes in the changes_in_PnL list
        if total_number_of_months > 1:
            change = monthly_profit_and_loss - previous_profit_and_loss
            changes_in_PnL.append(change)
        # the below will store the previous months profit and loss for the next for loops iteration
    
            if change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = change
            if change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = change
    
        previous_profit_and_loss = monthly_profit_and_loss
    
# len counts the number of items in a list     
    # print(len(date))        
    # print(sum(profit_and_loss))
    # print(sum(changes_in_PnL)/(len(changes_in_PnL)))
    # print(greatest_decrease)
    # print(greatest_increase)

# creates the file, allows the file to be written, then actually writes the file
T = "Analysis/PyBank Analysis.txt"    
with open(T, "w") as Budget_Data_Write:
    Budget_Data_Write.write("Financial Analysis\n")
    Budget_Data_Write.write("---------------------------------------------------\n")
    Budget_Data_Write.write(f"Total Months: {len(date)}\n")
    Budget_Data_Write.write(f"Total: ${sum(profit_and_loss)}\n")
    Budget_Data_Write.write(f"Average Change: ${round(sum(changes_in_PnL)/(len(changes_in_PnL)),2)}\n")
    Budget_Data_Write.write(f"Greatest Increase in Profits: {greatest_increase}\n")
    Budget_Data_Write.write(f"Greatest Decrease in Profits: {greatest_decrease}\n")
     
 



        
        