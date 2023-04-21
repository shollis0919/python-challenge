import os
import csv

#Lists to hold month and profit/loss info
profitLoss =[]
month = []  

#Varibles for calculating results for regarding profits
total = 0  
monthCount = 0
GIncrease = 0
GDecrease =  0   
change = 0 

#Variables to determine index location in lists
index = 0
index1 = 0
index2 = 0


#Function that determines amount of money gained or lost betwwen 2 months based on which number is higher 
# and if it is a negative or positive number 
def profitCalc(x,y):
    m = 0
    if x < y and x < 0 and y > 0: # positve result
        m = abs(x) + abs (y)

    if x < y and x < 0 and y < 0: # positive result
        m = abs(x) - abs (y)

    if x < y and x > 0 and y > 0: # positive result
        m = abs(y) - abs (x)

    if x > y and x < 0 and y < 0: # negative result
        m = abs(x) - abs (y)

    if x > y and x > 0 and y > 0: # negative result
        m = abs(y) - abs (x)
    
    if x > y and x > 0 and y < 0: # negative result
        m = ((abs(x) + abs (y))*-1)
    return m

#Open and read through the CSV file
csvpath = os.path.join('..' , 'PyBank', 'Resources', 'budget_data.csv')

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')
    csv_header = next(csvfile)

    #Writting info from CSV into lists and totaling amount in row 1
    for row in csvreader:
        total = total + int(row[1])
        monthCount = monthCount +1
        profitLoss.append(row[1])
        month.append(row[0])

    #Zip profitLoss list with itself to make pairs for use with the function
    for x,y in zip(profitLoss, profitLoss[1:]):

        #Calculation total change and storing place in index
        change = change + profitCalc(int(x),int(y))
        index = index + 1

        #Putting list through profitCalc() function when greatest decrease and increase is found
        #index is saved
        if profitCalc(int(x),int(y)) > GIncrease:
            GIncrease = profitCalc(int(x),int(y))
            index1 = index
            
        if profitCalc(int(x),int(y)) < GDecrease:
            GDecrease = profitCalc(int(x),int(y))
            index2 = index

    #Avergage change is calculated
    changeAvg = round(change / (monthCount-1),2)

    #All results are exported to a .txt file
    with open('BugetResults.txt','w') as f:
        print("Financial Analysis",file=f)
        print("--------------------------------",file=f)
        print("Total Months: " + str(monthCount),file=f)
        print("Total: " + str(total),file=f)
        print("Average Change: " + "$"+ str(changeAvg),file=f)
        print("Greatest Increase in Profits: " + str(month[index1]) +" "+ str(GIncrease),file=f)
        print("Greatest Decrease in Profits: " + str(month[index2]) +" " + str(GDecrease),file=f)
        
    #Same results are printed to the terminal
    print("Financial Analysis")
    print("--------------------------------")
    print("Total Months: " + str(monthCount))
    print("Total: " + "$" +str(total))
    print("Average Change: " + "$"+ str(changeAvg))
    print("Greatest Increase in Profits: " + str(month[index1]) +" "+"$"+ str(GIncrease))
    print("Greatest Decrease in Profits: " + str(month[index2]) +" " +"$"+ str(GDecrease))

    
    



    


