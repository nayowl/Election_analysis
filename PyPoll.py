# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentages of votes each candidates won
# 4. The total number of each candidates won
# 5. The winner of election based on popular vote

# Import csv and os module.
import csv 
import os

#assign a variable to load a file from the path
file_to_load =os.path.join("Resources","election_results.csv")
# assign a variable to write a file to path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize total vote counter
total_votes=0
# add list for candidate name
candidate_options=[]
#add dictionary for counting votes for candidates
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open the election results and read the file
with open(file_to_load) as election_data:
    # to do : read and analyze data here
    # read the file object with reader function
    file_reader=csv.reader(election_data)
     # Read and print the header row.
    headers = next(file_reader)
     # Print each row in the CSV file.
    for row in file_reader:
        #add increment to total votes
        total_votes +=1
        # Print the candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
        # add candidate name to candidate option list
            candidate_options.append(candidate_name)
            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
             # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    # save to text file
    with open(file_to_save,"w") as txt_file:
        #print final count to terminal
        election_results=(
            f"\nElection Results\n"
            f"-----------------------------\n"
            f"Total votes : {total_votes:,}\n"
            f"-----------------------------\n"
        ) 
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)
        

        # Determine the percentage of votes for each candidate by looping through the counts.
        # 1. Iterate through the candidate list.
        for candidate_name in candidate_votes:
            #retrieve vote count for candidate
            votes=candidate_votes[candidate_name]
            #calculate the percentage of votes
            vote_percentage=float(votes)/float(total_votes)*100
            # print candidate name and percentage
            candidate_results=(f"{candidate_name} :  {vote_percentage:.1f} % ({votes:,}) \n")
            #print candidate result to terminal
            print(candidate_results)
            #write to textfile
            txt_file.write(candidate_results)
            # print(f"{candidate_name} :  {vote_percentage:.1f} % ({votes:,}) \n")

            # Determine winning vote count and candidate
            # 1. Determine if the votes are greater than the winning count.
            if (votes>winning_count) and (vote_percentage>winning_percentage):
            #if true than set winning count, winning percentage and winning candidate
                winning_count=votes
                winning_percentage=vote_percentage
                winning_candidate=candidate_name

            # print winning candidate
        winning_candidate_summary=(
                f"-----------------------------\n"
                f"Winner: {winning_candidate} \n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f} %\n"
                f"-----------------------------\n"
            )
        #write winning candidate to terminal
        print (winning_candidate_summary)
        #write winning candidate to txt file
        txt_file.write(winning_candidate_summary)

