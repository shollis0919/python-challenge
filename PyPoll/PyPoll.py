import os
import csv


#Variables to hold vote counts
votes = 0
CCSVotes= 0
DDVotes = 0
RADVotes =0

#Opening CSV file to be read
csvpath = os.path.join('..' , 'PyPoll', 'Resources', 'election_data.csv')

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')
    csv_header = next(csvfile)


    #Looping through CSV to count total votes and votes for each candicate
    for row in csvreader:

        #Total vote count
        votes = votes +1

        #Individual candidate vote counts
        if row[2] == "Charles Casper Stockham":
            CCSVotes = CCSVotes + 1
        if row[2] == "Diana DeGette":
             DDVotes = DDVotes + 1
        if row[2] == "Raymon Anthony Doane":
             RADVotes = RADVotes + 1
    
    #Calculating percentage of candidate votes
    CCSPercent = round((CCSVotes/votes)*100,3)
    DDPercent = round((DDVotes/votes)*100,3)
    RADPercent  = round((RADVotes/votes)*100,3)

    #Exporting results to a .txt file
    analysisFilePath = "/Analysis/PollResults.txt"
    with open(analysisFilePath,'w',) as f:
        print("Election Results",file=f)
        print("-------------------------",file=f)
        print("Total Votes: " + str(votes),file=f)
        print("-------------------------",file=f)
        print("Charles Casper Stockham: " + str(CCSPercent)+ "% (" + str(CCSVotes)+")",file=f)
        print("Diana DeGette: " + str(DDPercent)+ "% (" + str(DDVotes)+")",file=f)
        print("Raymon Anthony Doane: " + str(RADPercent)+ "% (" + str(RADVotes)+")",file=f)

        print("-------------------------",file=f)

        #Using conditionals to determine the winner and printing results
        if CCSPercent > DDPercent and CCSPercent > RADPercent:
            print("Winner: Charles Casper Stockham",file=f)
        if DDPercent > CCSPercent and DDPercent > RADPercent:
            print("Winner: Diana DeGette",file=f)
        if RADPercent > DDPercent and RADPercent > CCSPercent:
            print("Winner: Raymon Anthony Doane",file=f)
        print("-------------------------",file=f)

    #Printing the same results to the terminal
    print("Election Results")

    print("-------------------------")

    print("Total Votes: " + str(votes))
    print("-------------------------")
    print("Charles Casper Stockham: " + str(CCSPercent)+ "% (" + str(CCSVotes)+")")
    print("Diana DeGette: " + str(DDPercent)+ "% (" + str(DDVotes)+")")
    print("Raymon Anthony Doane: " + str(RADPercent)+ "% (" + str(RADVotes)+")")

    print("-------------------------")

    if CCSPercent > DDPercent and CCSPercent > RADPercent:
        print("Winner: Charles Casper Stockham")
    if DDPercent > CCSPercent and DDPercent > RADPercent:
        print("Winner: Diana DeGette")
    if RADPercent > DDPercent and RADPercent > CCSPercent:
        print("Winner: Raymon Anthony Doane")

    print("-------------------------")





