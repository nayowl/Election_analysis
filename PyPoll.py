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
# open the election results and read the file
with open(file_to_load) as election_data:
    # to do : read and analyze data here
    # read the file object with reader function
    file_reader=csv.reader(election_data)
     # Read and print the header row.
    headers = next(file_reader)
    print(headers)