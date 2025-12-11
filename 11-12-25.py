import pandas as pd 
import statsmodels.api as sm
import seaborn as sns 
import matplotlib.pyplot as plt 

job_satisfaction = pd.read_csv("C:/Users/USER/Downloads/employee_satisfaction.csv")
work_units = pd.read_csv("C:/Users/USER/Downloads/employee_work_unit.csv")

job_satisfaction = job_satisfaction.merge(work_units, on['employee_id', 'manager'])

job_satisfaction['salary'].str.replace('\$|,', '', regex=True).astype(float)

sm.formula.ols('overallSatisfaction ~ salary', job_satisfaction).fit().summary()

sdsa_columns = [col for col in job_satisfaction.columns if col.endswith('SDSA')]

job_melt = job_satisfaction.melt(
    id_vars=['employee_id', 'overallSatisfaction'], #(dont want to melt)
    value_vars=sdsa_columns
)

sns.boxplot(job_melt, x='value', y= 'overallSatisfaction', hue='variable')

plt.show()

year_scores = pd.read_csv("C:/Users/USER/Downloads/year_scores.csv")

year_scores.groupby('id').size()

year_scores = year_scores.sort_values("year")

year_scores['seq_values'] = year_scores.groupby('id').cumcount() + 1

year_scores = year_scores.sort_values(['id', 'seq_values'])

year_pivot = year_scores.pivot(
    values='score',
    index='id',
    columns='seq_values'
)
year_pivot

year_pivot.columns = [f'score_year_{col}' for col in year_pivot.columns]

class_data = pd.read_csv("C:/Users/USER/Downloads/class_data - Sheet1.csv")
class_data['things_you_like'].unique()
class_data['things_you_like'] = class_data['things_you_like'].str.lower()

class_data['things_you_like'] = class_data['things_you_like'].str.split(",")

exploded_data = class_data.explode('things_you_like')

exploded_data.pivot_table(index = exploded_data.index, columns='things_you_like', aggfunc='size', fill_value=0)

song_features = pd.read_csv('C:/Users/USER/Downloads/song_features.csv')
song_features.columns

song_features = song_features.drop(["uri", 'id', 'key', 'camelot', 'tempo',  'name', 'album'], axis = 1)
song_features.head()

song_pivot = song_features.pivot(
    values='popularity',
    index='song',
    columns= 'artist'
)

song_pivot

nba = pd.read_csv("C:/Users/USER/Downloads/nba_data.csv", encoding='latin1')
nba.head()


nba_pivot = nba.pivot(
    values='PTS',
    index='Pos',
    columns= 'Player'
)

nba_pivot