# %% Result

# %% Tasks
'''
The dataframe is huge with many countries!

1. Find a way to subset the dataframe to only contain ASEAN countries. Here is a list of the ASEAN countries.

    ```python
    ASEAN_countries_list = [
    'Brunei', 'Burma', 'Cambodia',
    'Indonesia', 'Laos', 'Malaysia',
    'Philippines', 'Singapore', 'Vietnam']
    ```
'''

# %% Solution
from sys import argv  # Hide

import pandas as pd  # Hide

data_url = 'https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv'  # Hide
df_all = pd.read_csv(data_url)  # Hide

ASEAN_countries = [
    'Brunei', 'Burma', 'Cambodia',
    'Indonesia', 'Laos', 'Malaysia',
    'Philippines', 'Singapore', 'Vietnam'
]

# Where are the rows with the ASEAN countries?
filtered_ASEAN_rows = df_all['Country'].isin(ASEAN_countries)

# Select the ASEAN rows
df_ASEAN = df_all[filtered_ASEAN_rows]
df_ASEAN.head()
with open(f'{argv[0]}.html', 'w') as file:                 # Hide
    file.write(df_ASEAN.head().to_html())                  # Hide
