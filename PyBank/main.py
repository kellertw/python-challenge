#create file paths across operating systems
import os
#import dictionaries
import datetime
import collections
# CSV reading module
import csv
pybankpath_csv = 'budget_data.csv'

#pybankpath_csv = os.path.join("..","Resources", "/Users/owner/Bootcamp/GWU-ARL-DATA-PT-12-2019-U-C/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv")
pathout = os.path.join("Resources", "budget_data_analysis.txt")
months= []
profit= []
with open(pybankpath_csv, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    csv_header = next(csvfile)
    for row in csvread:
        months.append(row[0])
        profit.append(int(row[1]))
total_months = len(months)
greatest_increase = profit[0]
greatest_decrease = profit[0]
total_profit = 0
total_profit_change= 0
for r in range(len(profit)):
    total_profit += profit[r]
    profit_change = int(profit[r]) - int(profit[r-1])
    if profit[r] >= greatest_increase:
        greatest_increase = profit_change
        month_greatest_increase= months[r]
    if profit[r] <= greatest_decrease:
        greatest_decrease = profit_change
        month_greatest_decrease = months[r]
for r in range(len(profit)):
    total_profit_change += int(profit[r]) - int(profit[r- 1])
first_loop = (int(profit[0]) - int(profit[-1]))
total_profit_change_adj = total_profit_change - first_loop
average_profit_change = round((total_profit_change_adj)/(total_months-1),2)
output = (f"Financial analysis\n"
f".................................\n"
f"total_months:{total_months}\n"
f"total_profit:{total_profit}\n"
f'greatest_increase: {greatest_increase}\n'
f'month_great_increase: {month_greatest_increase}\n'
f'greatest_decrease: {greatest_decrease}\n'
f"month_greatest_decrease:{month_greatest_decrease}\n"
f'average_profit_change:{average_profit_change}')
print (output)
with open(pathout, "w") as txt_file:
    txt_file.write(output)
