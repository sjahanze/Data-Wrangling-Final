import pandas as pd

lyrics = pd.read_feather("C:/Users/USER/Downloads/lyrics_sample_2025.feather")

lyrics.dtypes

lyrics.iloc[0].T

lyrics['year'] = pd.to_datetime(lyrics['year'])

lyrics['year'].dtype

lyrics['y'] = lyrics['year'].dt.year

today = pd.Timestamp.today().normalize()

start_date = today - pd.DateOffset(years=15)

date_range = pd.date_range(
    start = start_date, 
    end=today, 
    freq='D'
)

lyrics_subset = lyrics[lyrics['year'].isin(date_range)]

lyrics_subset['lyrics']

lyrics_subset['fucks_given'] = lyrics_subset['lyrics'].str.count('[Ff]uck')

lyrics_subset['fuck_yes']= lyrics_subset['lyrics'].str.contains("[Ff]uck",regex = True)

lyrics_subset['fuck_yes']= lyrics_subset['fuck_yes'].apply(lambda x: 1 if x else 0)

lyrics_subset['fuck_yes'].sum()

import statsmodels.api as sm 
lyrics.columns

fuck_logit = sm.formula.logit('fuck_yes ~ genre + y', lyrics_subset).fit()
fuck_logit.summary()
import numpy as np
np.exp(fuck_logit.params)

fuck_logit = sm.formula.poisson('fucks_given ~ genre + y', lyrics_subset).fit()
fuck_logit.summary()

lyrics_subset.iloc[0].T

lyrics_subset['songwriter'].str.split(", ", regex = True, expand= True)

glass_door = pd.read_csv("C:/Users/USER/Downloads/glass_door.csv")
glass_door.head()

rankings = glass_door.groupby(['organization']).agg({'rating':'mean'})
rankings.columns
rankings['rating'].sort_values(ascending=False)

glass_subset = glass_door['review'].str.count("[Gg]ood")
glass_subset2 = glass_door['review'].str.contains("[Gg]ood")

glass_door = glass_door['review'].str.split('([A-Z]{4,7}: )', regex=True, expand=True)
glass_door.columns