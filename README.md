## Team Name: 
Project Team-2

## Project Idea 2 Title: 
Fantasy Football Team Creator
## Project Description:
Creates the ideal team based on currently available players. Users are recommended the top players based on the predicted score of each player based on linear regression models generated for each player. Allow users to browse player pools, view player details, and save players.
## Proposed Methodology/Resources:
### Resources:
7601 player stats from 2003 - 2017 with attributes:
Name, Pos, Team, Year, Games Plyd, Rush, Rush Yards, Rush TD, Target, Catch, Catch yards, Catch TD, Pass, Complete, Pass Yards, Pass TD, Int, Fum
http://thehuddle.com/fantasy_football_statistics_archive.php
### Methodology:
MySQL, Flask, Bootstrap, HTML/CSS
Identify players with high performance based on their predicted 2018 scores using multiple Linear Regression Models.

### AWS Hosted:

To use the Fantasy Football Team Creator on your web:
Run: 3.16.111.89

### To Run Locally:
1. Extract the zipped file in your location.
2. Run python db_data_load.py, to store the database in your MYSQL WorkBench.
3. Run python main.py, to launch the Fantasy Football Team Creator.
4. In your browser open https://localhost:5000 to access the system.
