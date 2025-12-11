import pandas as pd 
import timeit

nba = pd.read_csv("C:/Users/USER/Downloads/nba_data.csv", encoding = 'latin1')

nba_arrow = pd.read_csv("C:/Users/USER/Downloads/nba_data.csv", 
                        engine='pyarrow',
                        dtype_backend='pyarrow',
                        encoding= 'latin1')
