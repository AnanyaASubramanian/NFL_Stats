
import pandas as pd
import numpy as np


df = pd.read_csv('data/places.csv')
df = df[[ "Team",'latitude','longitude']]
df = df.sort_values('Team')
#df.to_csv('team.csv', index=False)


data = [['BUF','Buffalo Bills', 'AFC', 'East', 11, 6], 
['MIA','Miami Dolphins', 'AFC', 'East', 11, 6], 
['NYJ','New York Jets', 'AFC', 'East', 7,10], 
['NE','New England Patriots', 'AFC', 'East', 4, 13], 
['BAL','Baltimore Ravens', 'AFC', 'North', 13, 4],
['CLE', 'Cleveland Browns', 'AFC', 'North', 11, 6],
 ['PIT', 'Pittsburgh Steelers', 'AFC', 'North', 10, 7],
 ['CIN', 'Cincinnati Bengals', 'AFC', 'North', 9, 8],
 ['HOU', 'Houston Texans', 'AFC', 'South', 10, 7],
 ['JAX', 'Jacksonville Jaguars', 'AFC', 'South', 9, 8],
 ['IND', 'Indianapolis Colts', 'AFC', 'South', 9, 8],
 ['TEN', 'Tennessee Titans', 'AFC', 'South', 6, 11],
 ['KC', 'Kansas City Chiefs','AFC', 'West', 11, 6], 
 ['LV', 'Las Vegas Raiders','AFC', 'West', 8, 9],
 ['DEN', 'Denver Broncos','AFC', 'West', 8, 9],
 ['LAC', 'Los Angeles Chargers','AFC', 'West', 5, 12],
 ['DAL','Dallas Cowboys', 'NFC', 'East', 12, 5], 
['PHI', 'Philadelphia Eagles', 'NFC', 'East', 11, 6], 
['NYG','New York Giants', 'NFC', 'East', 6, 11], 
['WAS','Washington Commanders', 'NFC', 'East', 4, 13], 
['DET','Detroit Lions', 'NFC', 'North', 12, 5],
['GB', 'Green Bay Packers', 'NFC', 'North', 9, 8],
 ['MIN', 'Minnesota Vikings', 'NFC', 'North', 7,10],
 ['CHI', 'Chicago Bears', 'NFC', 'North', 7, 10],
 ['TB', 'Tampa Bay Buccaneers', 'NFC', 'South', 9, 8],
 ['NO', 'New Orleans Saints', 'NFC', 'South', 9, 8],
 ['ATL', 'Atlanta Falcons', 'NFC', 'South', 7, 10],
 ['CAR', 'Carolina Panthers', 'NFC', 'South', 2, 15],
 ['SF', 'San Francisco 49ers','NFC', 'West', 12, 5], 
 ['LAR', 'Los Angeles Rams','NFC', 'West', 10, 7],
 ['SEA', 'Seattle Seahawks','NFC', 'West', 9, 8],
 ['ARI', 'Arizona Cardinals','NFC', 'West', 4, 13]]


df = pd.DataFrame(data, columns=['Abbreviation', 'Team', 'Conference', 'Division', 'Wins', 'Losses'])

df = df.sort_values('Team')
#df.to_csv('nfl_teams.csv', index=False)

nfl_teams = pd.read_csv('data/nfl_teams.csv')
sorted_teams = pd.read_csv('data/team.csv')
merged = nfl_teams.merge(sorted_teams, on='Team')
#merged.to_csv('data/MergedTeam.csv', index=False)

import pandas as pd

df = pd.read_csv('data/MergedTeam.csv')

sf_49ers = pd.DataFrame([{
    'Abbreviation': 'SF',
    'Team': 'San Francisco 49ers',
    'Conference': 'NFC',
    'Division': 'West',
    'Wins': 12, 
    'Losses': 5,  
    'latitude': 37.7749,  
    'longitude': -122.4194  
}], columns=['Abbreviation', 'Team', 'Conference', 'Division', 'Wins', 'Losses', 'latitude', 'longitude'])

df = pd.concat([df, sf_49ers], ignore_index=True)

#df.to_csv('MergedTeam.csv', index=Falsed)
#this created all the qb csv files.
'''
qbs = df['QB'].unique()
qbname = pd.DataFrame()
for qb in qbs:
    qbname.to_csv(f'{qb}.csv', index=False)
'''

df_stadium = pd.read_csv('data/Stadium.csv')
df_teams = pd.read_csv('data/MergedTeam.csv')
df_merged = pd.merge(df_teams, df_stadium, on='Team')
#df_merged.to_csv('MergedTeam.csv', index=False)