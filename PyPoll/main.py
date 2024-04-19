# Importing modules 
import os
import csv
import collections

# Reading csv file and txt file
ELECTION_Poll = os.path.join("Resources", "election_data.csv")
OUTPUT_poll = os.path.join("Analysis", "output.txt")

# Return the absolute path to script file
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# make a dictionary of items, variables into collection
candidate_elect = collections.Counter()

with open(ELECTION_Poll) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Stores the header row
    next(csvreader) 
    for row in csvreader:
        # Count each vote + update the dictionary
        candidate_elect[row[2]] += 1

# The total votes cast
total_v = candidate_elect.total()

# The percentage and total number 
votes_per_elect = ""
for elect, votes in candidate_elect.items():
    percent_votes = round((votes/total_v) * 100, 3)
    votes_per_elect += f"{elect}: {percent_votes}% ({votes})\n"
    # The winner with popular vote
    try:
        if votes > popular_votes:
            popular_votes = votes
            winner = elect
    except NameError:
        popular_votes = votes

# Election Results variable
output = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_v}\n"
    "-------------------------\n"
    f"{votes_per_elect}\n"
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print results to txt file
print(output)
with open(OUTPUT_poll, 'w') as outputfile:
    outputfile.write(output)