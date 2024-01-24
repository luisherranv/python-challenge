# Modules
import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

MonthCount = 0
TotalProfLoss = 0
ProfLoss = 0
ProfLoss = []
Month = []
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        #Determine the number of colums in CSV file = Number of Months
        MonthCount += 1
        #Determine the total profit/losses
        TotalProfLoss += int(row[1])
        #Create a list with the values of Profits and Losses and Month
        ProfLoss.append(int(row[1]))
        Month.append(row[0])

count = 0
avgROC = 0
TotalROC = 0
ProfLossROC = []
for i in range(MonthCount-1):
    #Calculate the change between each month
    ProfLossROC.append((ProfLoss[count+1]-ProfLoss[count]))
    #Add all of the changes
    TotalROC += ProfLossROC[i]
    count += 1
#Calculate the average rate of change
avgROC = TotalROC/(MonthCount-1)

print(" ")
print("Financial Analysis")
print(" ")
print("----------------------------")
print(" ")
print(f'Total Months: {MonthCount}')
print(" ")
print(f'Total: ${TotalProfLoss}')
print(" ")
print(f'Average Change: ${avgROC:.2f}')
print(" ")
#Determine the min and max, and use their indexes to determine the respective month
print(f'Greatest Increase in Profit: {Month[ProfLossROC.index(max(ProfLossROC))+1]} ${max(ProfLossROC)}')
print(" ")
print(f'Greatest Increase in Profit: {Month[ProfLossROC.index(min(ProfLossROC))+1]} ${min(ProfLossROC)}')
print(" ")
    

