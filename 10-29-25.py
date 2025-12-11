import pandas as pd
import statsmodels.api as sm
import seaborn as sns 
import re 

rail = pd.read_csv("C:/Users/USER/Downloads/Rail_Equipment_Accident_Incident_Data.csv")

col_list = rail.columns.to_list()

keepers = [bool(re.search(r'Killed|Injured|Cost', col))for col in col_list]

rail_cols = rail.columns[keepers]

rail_cols = rail_cols.append(pd.Index(["Report Year"]))

rail = rail[rail_cols]

rail = rail[(rail['Total Persons Killed'] > 0) & (rail['Total Persons Injured'] > 0)]

rail['Total Damage Cost'] = rail['Total Damage Cost'].str.replace(',', '').astype(float)

rail[rail['Total Damage Cost'].between(50000, 1000000)]

rail.loc[rail['Total Damage Cost'].idxmax()]

bootstrap_samples = 100

t_values = []

for i in range(bootstrap_samples):
    sample = rail.sample(frac = 1, replace = True)
    model = sm.formula.ols('Q("Total Damage Cost") ~ Q("Total Persons Killed")', data = sample)
    t_val = model.fit().tvalues['Q("Total Persons Killed")']
    t_values.append(t_val)

import matplotlib.pyplot as plt
sns.histplot(t_values)
plt.show()