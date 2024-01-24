# Modules
import os
import csv

csvpath = ("Resources", "election_data.csv")

TotalVotes = 0
AllCandidates = []
Candidates = []
#Determine total votes and the repeated candidate names
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        TotalVotes += 1
        AllCandidates.append(row[2])
        # if the values in column [1] are not in candidates, add them
        if row[2] not in Candidates:
            Candidates.append(row[2])
        #if they are in candidates, nothing happens
        else: 
            pass
print("")
print("Election Results")
print("")
print("-----------------------------")
print("")
print(f'Total Votes: {TotalVotes}')
print("")
print("-----------------------------")
print("")
TotalPCandidate = [] #total per candidate
PerPCandidate = [] #percentace per candidate
#Count the times that each candidate repeats in the list of all candidates
for i in range(len(Candidates)):
    TotalPCandidate.append(AllCandidates.count(Candidates[i]))
    #Calculate percentage
    PerPCandidate.append(int(TotalPCandidate[i])/TotalVotes*100)
    print(f'{Candidates[i]}: {PerPCandidate[i]:.3f}% ({TotalPCandidate[i]})')
    print("")
print("-----------------------------")
print("")
print(f'Winner: {Candidates[PerPCandidate.index(max(PerPCandidate))]}')
print("")
print("-----------------------------")
print("")
