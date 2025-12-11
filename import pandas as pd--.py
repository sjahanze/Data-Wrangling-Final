import pandas as pd
nba = pd.read_csv("C:/Users/USER/Downloads/nba_pbp_14_24.csv")
nba
nba.loc[1].T

nba['shooter'] = nba['shooter'].str.replace('\s$', '', regex = True) #\s represents white space

nba.groupby(['gameID', 'shooter']).size().reset_index(name='counts') #Size counts how many times they appear

nba.groupby(['gameID', 'shooter'])['result'].value_counts().unstack(fill_value=0).reset_index()

nba.groupby('shooter').agg({'distance': ['mean', 'std'], 'assist': 'count'}).reset_index()