## Team Name: 
Project Team-2
## Project Title: 
High Risk Accident Areas
## Project Description:
Using Google Maps and nearest neighbor algorithms, the application will cluster different areas of Maryland into various classes of risk zones.  
## Comments: Why just Meryland? do you have datasets available for bay area?  - APPROVED if you can do for bay area
## Proposed Methodology/Resources:
### Resources:
A crash dataset consisting of 77,791 rows and attributes:
Report Number, Local Case Number, Agency Name, ACRS Report Type,	Crash Date/Time, Route Type, Road Name,	Cross-Street Type,	Cross-Street Name, Off-Road Description, Municipality, Related Non-Motorist, Collision Type, Weather, Surface Condition, Light, Traffic Control, Driver Substance Abuse, Non-Motorist Substance Abuse, Person ID, Driver At Fault, Injury Severity, Circumstance, Driver Distracted By,Drivers License State,	Vehicle ID, Vehicle Damage Extent, Vehicle Body Type, Vehicle Movement, Latitude, Longitude, and Location
### Methodology:
Node.js, Express, and MongoDB
Classify clusters using various nearest neighbors algorithms such as kNN, LSH. Use Google Maps API to visualize data as well as clusters.


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
