# We are using python to analyze financial records of the company. We are given a dataset called "budget_data".

#importing the modules
import os
import csv

#Makingn the csv file readable in python
budget_data = os.path.join("Resources","budget_data.csv")
OutPutData = os.path.join ("Analysis", "Output.txt")

# My variables
total_Month = 0
total_PL = 0
Change = 0
dates = []
profits = []
value = 0


with open (budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Header row
    csv_header = next(csvreader)
    
    #Read the first row
    first_row = next(csvreader)
    total_Month += 1
    total_PL += int(first_row[1])
    value = int(first_row[1])

    # Through each row data
    for row in csvreader:
        # Keep track of the dates
        dates.append(row[0])
        
        # Calculate the change, add to list of changes
        Change = int(row[1])-value
        profits.append(Change)
        value = int(row[1])
        
        # total of months
        total_Month += 1
        
        # Total amount "profit/losses entire period"
        total_PL = total_PL + int(row [1])
        
    # Greatest increase 
    Greatest_Increase = max(profits)
    Greatest_index = profits.index(Greatest_Increase)
    Greatest_Date = dates[Greatest_index]
    
    # Greatest decrease
    Greatest_Decrease = min(profits)
    Decrease_index = profits.index(Greatest_Decrease)
    Worst_Date = dates[Decrease_index]
    
    # Average change in "Profit/Losses"
    Avg_change = sum(profits)/len(profits)
    
# Financial Analysis Display
print("Financial Analysis")
print("------------------")
print(f"Total Months: {str(total_Month)}")
print(f"Total: ${str(total_PL)}")
print(f"Average Change: ${str(round(Avg_change, 2))}")
print(f"Greatest Increase in Profits: {Greatest_Date} (${str(Greatest_Increase)})")
print(f"Greatest Decrease in Profits: {Worst_Date} (${str(Greatest_Decrease)})")

output = (
    "Financial Analysis\n"
    "-----------------------"
    f"Total Months: {total_Month}\n"
    f"Total: {total_PL}\n"
    f"Average Change: ${Avg_change}\n"
    f"Greatest Increase in Profits: {Greatest_Date} (${Greatest_Increase})\n"
    f"Greatest Decrease in Profits: {Worst_Date} (${Greatest_Decrease})\n"

)
# Print Output text
print(output)
with open (OutPutData, 'w') as outputfile:
    outputfile.write(output)
    
# Create output file
OP_file = os.path.join("ResultPYbank.csv")
with open(OP_file, "w", newline="") as datafile:
     writer = csv.writer(datafile)
     
     # write output file
     writer.writerow(["Financial Analysis"])
     writer.writerow(["-----------------------"])
     writer.writerow([f'Total Months: {total_Month}'])
     writer.writerow([f'Total: ${total_PL}'])
     writer.writerow([f'Average Change: ${Avg_change}'])
     writer.writerow([f'Greatest Increase in Profits: {Greatest_Date} (${Greatest_Increase})'])
     writer.writerow([f'Greatest Decrease in Profits: {Worst_Date} (${Greatest_Decrease})'])