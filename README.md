# python-challenge

2 python scripts were made to perform numerical analysis on the CSV's provided in the assignment.
Inside the repository are 2 python scripts that are made for the CSV's proivided (budget_data and election_data). 2 text files that contain the results for both python scripts are included as well.


The following code was devised from 
for x,y in zip(profitLoss, profitLoss[1:]): https://stackoverflow.com/questions/21303224/iterate-over-all-pairs-of-consecutive-items-in-a-list


The following code was devised from: https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file

with open('BugetResults.txt','w') as f:
print("Financial Analysis",file=f)
print("Total Months: " + str(monthCount),file=f)
print("Total: " + str(total),file=f)
print("Average Change: " + "$"+ str(changeAvg),file=f)
print("Greatest Increase in Profits: " + str(month[index1]) +" "+ str(GIncrease),file=f)
print("Greatest Decrease in Profits: " + str(month[index2]) +" " + str(GDecrease),file=f)
