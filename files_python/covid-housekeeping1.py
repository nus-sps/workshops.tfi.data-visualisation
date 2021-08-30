# %% Result

# %% Tasks
'''
The dataframe is huge with many countries!

1. Load the data from https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv

2. What is the shape of the data? I.e. how many rows and columns are there?

3. Are there any missing numbers?

4. What are column names?
'''

# %% Solution
import pandas as pd  # Hide
from sys import argv  # Hide

data_url = 'https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv'
df = pd.read_csv(data_url)

#df.shape

#df.columns

#df.describe()

#df.info()

df.head()

with open(f'{argv[0]}.html', 'w') as file:                 # Hide
    file.write(df.head().to_html())                  # Hide
