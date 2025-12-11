import pandas as pd 

songs = pd.read_csv("C:/Users/USER/Downloads/songs_200.csv")
features = pd.read_csv("C:/Users/USER/Downloads/features_200.csv")

pd.concat([songs, features], axis = 1)

songs.merge(right=features, how='left', left_on='artist_x', right_on='artist')

test_merge = pd.merge(songs, features, how='left', left_on='artist_x', right_on='artist')

test_merge['artist'].duplicated()

test_merge.loc[test_merge['artist'].duplicated(), ['artist_x', 'song_x', 'duration']]

test_merge = pd.merge(songs, features, how='left', left_on=['artist_x', "song_x"], right_on=['artist', 'song'])


test_merge.loc[test_merge['artist'].duplicated(), ['artist_x', 'song_x', 'duration']]

duplicated_records = test_merge['artist'].duplicated()

test_merge[~duplicated_records]

test_merge.drop_duplicates()['song_x'].value_counts()

songs['joiner'] = songs["artist_x"] + "_" + songs["songs_x"]
features = features["artist"] + "_" + features["songs"]

artist_name = pd.read_csv("C:/Users/USER/Downloads/artist_name.csv")
artist_networth = pd.read_csv("C:/Users/USER/Downloads/artist_net_worth.csv")
artist_no1hits = pd.read_csv("C:/Users/USER/Downloads/artist_number_one_hits.csv")
artist_albums = pd.read_csv("C:/Users/USER/Downloads/artist_studio_albums.csv")
artist_thits = pd.read_csv("C:/Users/USER/Downloads/artist_top_hits.csv")

merge1 = pd.merge(artist_name, artist_networth, how="left", left_on="Artist", right_on='Artist')
merge2 = pd.merge(merge1, artist_albums, how= 'left', left_on= "Artist", right_on= "Artist")
merge3 = pd.merge(merge2, artist_thits, how='left', left_on= 'Artist', right_on= 'Artist')
artist_final = pd.merge(merge3, artist_no1hits, how= 'left', left_on= 'Artist', right_on='artist')
del artist_final['artist'] 
artist_final

artist_duplicated = artist_final.duplicated()
artist_final_data = artist_final.drop_duplicates()
artist_final_data.duplicated()


# Separate manager column (categorical) from numeric columns
numeric_cols = e_satisfaction.select_dtypes(include=['int64','float64']).columns

e_satisfaction_agg = (
    e_satisfaction
    .groupby('employee_id')[numeric_cols]
    .mean()
    .reset_index()
)

merge1 = pd.merge(e_age, e_satisfaction_final, on="employee_id", how="left")
merge2 = pd.merge(merge1, e_wunit, on="employee_id", how="left")
merge3 = pd.merge(merge2, m_ratings, left_on="manager", right_on="manager_id", how="left")

merge3.head()
