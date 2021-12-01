# import os moduile
import os

# import modile for reading the csv
import csv

#set the variables for
#The total number of months included in the dataset
total_months = 0

#The net total amount of "Profit/Losses" over the entire period
net_total = 0

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
date_average = []
month_count = []
#The greatest increase in profits (date and amount) over the entire period
greatest_increase_profit = 0
greatest_increase_date = 0

#The greatest decrease in profits (date and amount) over the entire period
greatest_decrease_profit = 0
greatest_decrease_date = 0

# reading the csv file
budget_data = os.path.join(".","Resources","budget_data.csv")

# with open(budget data) as csv file
with open(budget_data,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
# find the header row and skip if there isn't a header
    csv_header = next(csvreader)
    row = next(csvreader)
    
# calc the months and work out the p&l
    previous_row = int(row[1])
    total_months += 1
    net_total += int(row[1])
    greatest_increase_profit = int(row[1])
    greatest_increase_date = row[0]
    
# read each row under header
    for row in csvreader:

# total months/the total amount
        total_months += 1
        net_total += int(row[1])

# calcualte the difference from the previous date
        profit_change = int(row[1]) - previous_row
        date_average.append(profit_change)
        previous_row = int(row[1])
        month_count.append(row[0])

#The greatest increase in profits (date and amount) over the entire period
        if int(row[1]) > greatest_increase_profit:
            greatest_increase_profit = int(row[1])
            greatest_increase_date= row[0]

#The greatest decrease in profits (date and amount) over the entire period
        if int(row[1]) < greatest_decrease_profit:
            greatest_decrease_profit = int(row[1])
            greatest_decrease_date = row[0]  
        
#average of all the changes
    average_change = sum(date_average)/len(date_average)
    
    highest = max(date_average)
    lowest = min(date_average)

# print the information as the example in the instructions
print(f"Financial Analysis")
print(f"-------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_date}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_date}, (${lowest})")

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
# print the file into the analysis folder
output_file = os.path.join(".", "analysis","analysis.txt")

# write the file in open mode
with open(output_file, 'w',) as txtfile:

# write analysis into the text file
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"-------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average  Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_date}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_date}, (${lowest})\n")