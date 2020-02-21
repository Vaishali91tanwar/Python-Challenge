import os
import csv

#Declaration of list and dictionary used for storing information
votes=[]
candidates=[]
candidate_vote={}
candidate_percentage={}

#Calculating the total votes received 
def total_votes(row):
    votes.append(row[2])

#Storing the unique candidates in a list and creating a dictionary with uique names as keys and initialising their vote count to zero
def unique_candidates(list):
    for i in range(len(list)):
        if list[i] not in candidates:
            candidates.append(list[i])
            candidate_vote[list[i]]=0


#Calculating the total votes received by each candidate and storing in candidate_vote dictionary
def count_votes(list):
    for i in range(len(list)):
        for d in candidate_vote:
            if list[i]==d:
                candidate_vote[d]=int(candidate_vote[d])+1

#Calculating the percentage of votes received by each candidate
def percentage_vote(dict):
    for d in dict:
        candidate_percentage[d]=format(int(dict[d])/len(votes)*100,".3f")
        


#Determinig the winner's name
def winner(dict):
    max=0
    for d in dict:
        if dict[d]>max:
            max=dict[d]                
            name=d
    return name


#Reading the csv file
csvpath= os.path.join("03-Python_Instructions_PyPoll_Resources_election_data.csv")
with open(csvpath,  newline="") as csvfile:
    csvreader=csv.reader(csvfile)
    csv_header=next(csvreader)
    for row in csvreader:
        total_votes(row)

#Calling of functions
unique_candidates(votes)
count_votes(votes)
percentage_vote(candidate_vote)
winner_name=winner(candidate_vote)

#Printing the result to the terminal
print("Election Results")
print("------------------------")
print(f"Total Votes: {len(votes)}")
print("------------------------")
for d in candidate_vote:
    print(f"{d}: {candidate_percentage[d]}% ({candidate_vote[d]})")
print("------------------------")
print(f"Winner: {winner_name}")



#Writing the output to the text file textPyPoll
file=open("textPyPoll.txt","w")
string1="Election Results\n-----------------------\nTotal votes: "+str(len(votes))+"\n-----------------------\n"
file.write(string1)
for d in candidate_vote:
    string2=d+": "+str(candidate_percentage[d])+"% ("+str(candidate_vote[d])+")\n"
    file.write(string2)
string3="-----------------------\n"+"Winner: "+winner_name
file.write(string3)
file.close()

