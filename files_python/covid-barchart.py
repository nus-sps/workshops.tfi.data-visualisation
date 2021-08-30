# %% Result

# %% Tasks
'''
1. Subset the dataset so that it contains only the latest date of each country.

2. Using either `pandas` or `matplotlib` or both, plot the total number of deaths in each country.

3. Is there a better way to represent this plot?
**Hint**: Maybe make the barchart descending!
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


plt.figure(figsize=(5, 5)) # Hide

# Pandas Manipulation #
latest_date = max(df_ASEAN['Date'])
df_ASEAN_latest_date = df_ASEAN[df_ASEAN['Date'] == latest_date]
df_ASEAN_latest_date.set_index('Country', inplace = True)
df_ASEAN_latest_date.sort_values(by = 'Deaths', ascending=True, inplace = True)

# Plotting #
ax = df_ASEAN_latest_date['Deaths'].plot(kind = 'barh')

# Pretty Things #
ax.set_xlabel('Total Deaths', fontsize = 10)
ax.set_ylabel('Country', fontsize = 10)
ax.set_title('Number of Deaths due to COVID-19 by countries', fontsize = 10)
plt.xticks(fontsize = 7)
plt.yticks(fontsize = 7)
plt.tight_layout()
plt.savefig(f'{argv[0]}.png', dpi=150)  # Hide
plt.show()
