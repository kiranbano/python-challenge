import os
import csv
import math

candidatelist = []
unique_candidate = []
vote_count = []
count = 0
vote_percent = []

csvpath = os.path.join("..", "Documents", "PyPoll.csv")


with open("PyPoll.csv", 'r', newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    csv_header = next(rows)
     
    for row in rows:
        count = count + 1
        candidatelist.append(row[2])
    for x in set(candidatelist):
        unique_candidate.append(x)
        y = candidatelist.count(x)
        vote_count.append(y)
        z = (y/count)*100
        vote_percent.append(z)
        
    
        
    # list_candidates = candidates.keys()
    
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)] 
    
    
print("Election Results\n")   
print("------------------------------------\n")
print(f"Total Votes: {count}\n")
print("------------------------------------\n")
for i in range(len(unique_candidate)):
    print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
    # print(f"{unique_candidate[i]}: {vote_percent[i]}% ({vote_count[i]})")
print("------------------------------------\n")
print(f" The winner is : {winner}")
print("------------------------------------\n") 

with open("Election Results", "w") as outfile:
    outfile.write("Election Results\n")   
    outfile.write("------------------------------------\n")
    outfile.write(f"Total Votes: {count}\n")
    outfile.write("------------------------------------\n")
    for i in range(len(unique_candidate)):
        outfile.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
        # print(f"{unique_candidate[i]}: {vote_percent[i]}% ({vote_count[i]})")
    outfile.write("------------------------------------\n")
    outfile.write(f" The winner is : {winner}")
    outfile.write("------------------------------------\n") 