#import the os module that will allow us to create file paths across operating systems
import os

#import module for reading the csv file
import csv

csvpath = os.path.join(r"C:\Users\marie\Documents\KU_Bootcamp\Python_Challenge\Starter_Code\Starter_Code\PyBank\Resources\Budget-Data.csv")

#establish lists that go through the rows to find Profit, Months, and Profit Change
profit = []
months = []
profit_change = []

#open csv file to read
with open(csvpath, 'r', newline= '', encoding= 'utf-8') as forecast:


    #put the file Budget-Data.csv into a variable
    csv_reader = csv.reader(forecast, delimiter = ",")

    #skip the header
    header = next(csv_reader)

    #navigate through the rows in the file
    for row in csv_reader:

        #attach months and profit to their established lists
        profit.append(int(row[1]))
        months.append(row[0])

    #navigate through profits looking for the monthly changes
    for d in range(len(profit)-1):

        #use the difference between months and attach to profit change
        profit_change.append(profit[d+1]-profit[d])

#find the min and max
value_min = min(profit_change)
value_max = max(profit_change)

#link the min and max with the correct month using the profit_change lists
monthly_increase = profit_change.index(min(profit_change)) + 1
monthly_decrease = profit_change.index(max(profit_change)) + 1

#print out statements
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {months[monthly_increase]} (${(str(value_max))})")
print(f"Greatest Decrease in Profits: {months[monthly_decrease]} (${(str(value_min))})")

#output
output = os.path.join(r"C:\Users\marie\Documents\KU_Bootcamp\Python_Challenge\Summary.txt")
with open(output, "w") as file:

#right out summary results in new file
   file.write("Financial Analysis")
   file.write("\n")
   file.write("---------------------------")
   file.write("\n")
   file.write(f"Total Months: {len(months)}")
   file.write("\n")
   file.write(f"Total: ${sum(profit)}")
   file.write("\n")
   file.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
   file.write("\n")
   file.write(f"Greatest Increase in Profits: {months[monthly_increase]} (${(str(monthly_increase))})")
   file.write("\n")
   file.write(f"Greatest Decrease in Profits: {months[monthly_decrease]} (${(str(monthly_decrease))})")




