# Election_analysis

## 1. Project Overview

A Colorado Board of Election employee has given the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Get a complete list of county.
4. Calculate the total number of votes each county received.
5. Calculate the percentage of votes each county.
6. Determine the county with the largest number of voters
7. Calculate the total number of votes each candidate received.
8. Calculate the percentage of votes each candidate won
9. Determine the winner of the election based on popular vote

## 2. Resources 
- Data Source : election_results.csv
- Software: Python 3.7.6,Visual Studio Code , 1.38.1

## 3. Results
The current dataset has 1 sheet and  3 columns consisting of Ballot ID, County and Candidate. 

The result of the analysis will be displayed in the terminal and written in election_result.txt  upon running the analysis in Visual Studio Code. Figure 1 shows us the result displayed in terminal, while Figure 2 shows us the result in txt file.
 
<img width="940" alt="election_results_terminal" src="https://user-images.githubusercontent.com/88597187/132413107-e39b72c4-b517-4ee9-b0d7-78f13fa5eba1.png">
<p align="center">
<sub>Figure 1 Election Result Displayed in Terminal </sub>
</p>

<p>&nbsp;</p>
<p>&nbsp;</p>

<img width="951" alt="election_results_txt" src="https://user-images.githubusercontent.com/88597187/132413116-1f7b9a95-067f-41de-b537-93029a088b58.png">
<p align="center">
<sub>Figure 2 Election Result Displayed in Txt File </sub>
</p>

<p>&nbsp;</p>

From the result above it can be summarized that:
- There were 369,711 votes cast in the election

  Total votes variable is set to 0, then read  each row in the csv file to determine the total. 
  ```
  # Initialize a total vote counter.
  total_votes = 0
  with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1
  ```
  
- There were 3 county in this election :
    - Jefferson
    - Denver
    - Arapahoe
  
- The total number and percentage for each county:
    - Jefferson received 10.5%  of the votes and 38,855 number of votes.
    - Denver received 82.8% of the votes and 306,055 number of votes.
    - Arapahoe received 6.7% of the votes and 24,801 number of votes.

To get the all of the participating county, a county list is created , read the csv file and append the county name to the county list if it doesn't currrently exist. Then to count the votes of each county  a dictionary  made to contain county names and county votes. Subsequently, the votes calculation  and percentage of each county will be added.
   ```
   # 1: Create a county list and county votes dictionary.
   county_list=[]
   county_votes_dict={}
   
   with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:
    
    # 3: Extract the county name from each row.
        county_name = row[1]
        
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes_dict[county_name]=0

        # 5: Add a vote to that county's vote count.
        county_votes_dict[county_name] += 1
        
    with open(file_to_save, "w") as txt_file:
       # 6a: Write a for loop to get the county from the county dictionary.
        for county_name in county_votes_dict:
        # 6b: Retrieve the county vote count.
           votes_county=county_votes_dict.get(county_name)
        # 6c: Calculate the percentage of votes for the county.
           votes_county_percentage=float(votes_county)/float(total_votes)*100
         # 6d: Print the county results to the terminal.
           county_results=(
            f"{county_name}: {votes_county_percentage:.1f}% ({votes_county:,})\n"
            )
           print(county_results)
        
         # 6e: Save the county votes to a text file.
           txt_file.write(county_results)

   ```
- County with the largest number of votes is Denver, which received 82.8% of the votes and 306,055 number of votes

To find the county with the largest number of votes,New Variables is created. Then using the calculation we already made from previous step, add condition in the loop, if the calculated  votes greater than largest_county_votes variable than it will be the value of the largest county votes. The condition will be added under the calculation to count votes and percentage.
```
# 2: Track the largest county and county voter turnout.
Largest_county=""
Largest_county_votes=0
Largest_county_percentage=0

         # 6e: Save the county votes to a text file.
           txt_file.write(county_results) #.... from the previous code
           if (votes_county>Largest_county_votes) and (votes_county_percentage>Largest_county_percentage):
              Largest_county=county_name
              Largest_county_votes=votes_county
              Largest_county_percentage=votes_county_percentage
```

- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results are:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes
 
To get the all of the participating candidates, we made list for the candidates , read the csv file and add the candidate name if the candidate name is not exist in the list ( this will be added under the coding for the county). Then to count the votes of each candidate,  we add dictionary to hold candidate name and candidate votes.  Subsequently, the votes calculation  and percentagefor each candidate will be added

```
# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}



    # 3: Extract the county name from each row.
        county_name = row[1] #...from the previous code
    #Get the candidate name from each row.
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1


       #....................add this under county calculation
       for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

    
```

- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes
 
To get the election winner. First we made variable to track it. Then using the calculation we already made from previous step, add condition in the loop, if the calculated  votes greater than  winning_count variable than it will be the value of the winner. The condition will be added under the calculation to count votes and percentage for candidates.

```
# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0


        #  Save the candidate results to our text file.
        txt_file.write(candidate_results) #.... from the previous code
        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage


```
  
 ## 4. Summary
Data analytic is one of powerful tool that can be utilized for election and planning election strategies. By using data analytic, it will be more accurate and efficient to count and analyze the data. Additionally, it can provide information and prediction for next election, therefore candidate can create relevant strategies and ensure the gain of the votes.

This election analysis is using Python and Visual Basic. These software are capable to calculate total votes, total number of votes and percentages each county received, determine the county with the largest votes, total number of votes and percentages of each candidate received and determine the winner of the election. Other election with the same format data source as the election_results.csv can be run in this analysis.  However,some improvements might be required if the format data source is different or there are changes in displayed result.  Some improvement which can be implemented in this code are:

- Additional field or replace existing field to use in another election type

For federal election purpose, the county can be replaced to state. Some fields such as party and polling station can be added too in  the data source, coding and displayed result. 

- Additional logic to help creating election strategy

The code can be modified to calculate how many votes and percentage candidate received for each county. This data can be helpful to devising strategy for the specific county, in order to increase the vote gains. With the additional field such as party and polling station, the code can be modified to calculate and display the votes and the  percentage each party received in each county/state or in polling station.

- Additional step to upload the data 

The data source of current analysis is only from single csv. However, if the election scale is big and has different data source, the code will need to be modified. All of .csv files can be moved into single directory and have the code modified to read all of the .csv data and merge it.

