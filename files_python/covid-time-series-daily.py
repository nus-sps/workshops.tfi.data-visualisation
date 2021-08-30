# %% Result

# %% Tasks
'''
Using the dataframe containing **ALL DATES** of ASEAN countries only:

1. Find the daily cases for each country using `.diff()`.

2. Set all negative values to NaN or 0s.

3. Plot the daily number of confirmed cases against dates.

4. Ensure that each country has their own `colour`.

5. Enable the legend
'''

# %% Solution
import pandas as pd  # Hide
from sys import argv  # Hide
import matplotlib.pyplot as plt # Hide

data_url = 'https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv'  # Hide
df_all = pd.read_csv(data_url)  # Hide

ASEAN_countries = ['Brunei', 'Burma', 'Cambodia',    'Indonesia', 'Laos', 'Malaysia',    'Philippines', 'Singapore', 'Vietnam'] # Hide

filtered_ASEAN_rows = df_all['Country'].isin(ASEAN_countries) # Hide

df_ASEAN = df_all[filtered_ASEAN_rows]                     # Hide

import numpy as np

# Pandas Manipulation #

df_ASEAN.loc[:, 'Daily'] = df_ASEAN['Confirmed'].diff()
df_ASEAN[df_ASEAN['Daily'] < 0] = np.NaN

# Plotting #
fig, ax = plt.subplots(figsize=(5, 5))

# Iterate through our countries so we can plot automatically plot them!
for country in ASEAN_countries:
    df_ASEAN_perCountry = df_ASEAN[df_ASEAN['Country'] == country]
    df_ASEAN_perCountry.plot('Date','Daily',ax=ax, label = country)

# Pretty Things #
plt.legend()
plt.ylabel('Number of Daily Cases', fontsize = 10)
plt.xlabel('Date', fontsize = 10)
plt.xticks(fontsize = 5)
plt.yticks(fontsize = 7)
plt.title('Number of Daily Cases over time in ASEAN countries', fontsize = 10)
plt.tight_layout()
plt.savefig(f'{argv[0]}.png', dpi=150)  # Hide
plt.show()

