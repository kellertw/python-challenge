#create file paths across operating systems
import os
import csv

# CSV reading module
pypollpath_csv = os.path.join("Resources", "election_data.csv")

# Create pathout
pathout = os.path.join("Resources", "poll_analysis.txt")

# Start Counter
vote_number = 0
winners_tally = 0
# Create lists to fill
candidates= []
tally = []
winner = ""

#read csv
with open(pypollpath_csv) as poll_data:
    csvread = csv.reader(poll_data, delimiter=',')
    csv_header = next(poll_data, None)

    #Create loop to process votes
    for row in csvread:
        # loader
        print(". ", end=""),
        
        # Total the votes
        vote_number = vote_number + 1
        
        # Candidate voted for
        candidate = row[2]

        #add votes to vote total
        if candidate in candidates:
            candidate_list = candidates.index(candidate)
            tally[candidate_list] = tally[candidate_list] + 1
        else:
            candidates.append(candidate)
            tally.append(1)
            
   
        # Percentage of vote for each candidate and the winner
        percentages = []
        vote_total = tally[0]
        index_max = 0

        for count in range(len(candidates)):
            vote_percent = tally[count]/vote_number*100
            percentages.append(vote_percent)
            if tally[count] > vote_total:
                vote_total = tally[count]
                print(vote_total)
                index_max = count
        winner = candidates[index_max]

# Round decimal

percentages = [round(i,2) for i in percentages]

#Print results
print("Voting Tally")
print("--------------------------")
print(f"Total Votes: {vote_number}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({tally[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

write_results = open(pathout, mode = "w")   

# Print to write file
write_results.write("Election Results\n")
write_results.write("--------------------------\n")
write_results.write(f"Total Votes: {vote_number}\n")
for count in range(len(candidates)):
    write_results.write(f"{candidates[count]}: {percentages[count]}% ({tally[count]})\n")
write_results.write("---------------------------\n")
write_results.write(f"Winner: {winner}\n")
write_results.write("---------------------------\n")

# Close file
write_results.close()