# mlb_player_value_analysis_2021
A collection of notebooks analyzing team and player value and performance analysis during the 2021 season

## How to Use this Application:

### File Structure
* player_values.ipynb houses an application that explores how to evaluate player performance based on salary during the 2021 season. It includes a function that will find the best players
for a given salary limit. It also determines the correlation for the 2021 season of player salary and WAR, player salary and service time, and service time and WAR. The application predominately finds
player values based on salary/WAR, ie. how much a player made per unit of production for the season. 
* batting_stats.ipynb is the precursor to the player_values.ipnyb notebook and was used to prototype some methods and data-cleanup for the player_values application.
* team_payrolls.ipynb houses the application that assesses which teams got the greatest value from their payrolls for the 2021 season looking at payroll and team record. 
* salaries.py provides some methods for data cleanup used in the player_values.ipynb notebook.

This application can be performed in Jupyter notebook using python version 3.7. The static_data directory houses the data from the 2021 season in csv and xlsx formats. Feel free to expand on this application and import your own data sources.
