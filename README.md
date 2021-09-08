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
The current dataset only has 1 sheet and  3 column consists of Ballot ID, County and Candidate. To know how the code is working , below is the step by step :
1. Define path where the data source and the result will be placed
```
# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join( "Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")

```
3. Setting Variable 


After running the analysis in Visual Studio Code, the result of the analysis will be displayed in the terminal and written in election_result.txt. Figure 1 shows us the result displayed in terminal, while Figure 2 shows us the result in txt file.
 
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

From the result above we can summarize that :
- There were 369,711 votes cast in the election
- There were 3 county in this election :
    - Jefferson
    - Denver
    - Arapahoe
- The total number and percentage for each county:
    - Jefferson received 10.5%  of the votes and 38,855 number of votes.
    - Denver received 82.8% of the votes and 306,055 number of votes.
    - Arapahoe received 6.7% of the votes and 24,801 number of votes.
- County with the largest number of votes is Denver, who received 82.8% of the votes and 306,055 number of votes
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results are:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes
  
 ## 4. Summary
Data analytic is one of powerful tool that can be utilized for election and planning election strategies. By using data analytic, it will be more accurate and efficient to count and analyze the data. In addition, it can provide information and prediction for next election, therefore candidate can create relevant strategies and ensure those votes were coming in. 

This election analysis is using Python and Visual Basic as the software. It can count total votes, total number of votes and percentages each county received, determine the county with the largest votes, total number of votes and percentages of each candidate received and determine the winner of the election. Other election with the same format data source as the election_results.csv can be run in this analysis.  But it will need some additional improvement if the format data source is different or there is change in displayed result.  Some improvement that can be implemented in this code are:

- Additional field or replace existing field to use in another election type

For federal election the county can be replaced to state, and we can add field like party and polling station in the data source, coding and displayed result. 

- Additional logic to help creating election strategy

To create strategy targeting for specific county, the code can be modified so it can count how many votes and percentage candidate received for each county. With the additional field like party and polling station, the code can be modified so it can count and display votes and percentage each party received in each county/state or in polling station.

- Additional step to upload the data 

For current analysis the data source is only from one csv. But if the election is big and has different data source, the code needs to be modified. We can put all the csv in one folder and then modified the code so it can read all the csv data in the folder and merge it.

