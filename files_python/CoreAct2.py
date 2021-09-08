# %% Result

# %% Solution
import pandas as pd  # Hide
from matplotlib import pyplot as plt # Hide
from sys import argv  # Hide

data_url = 'https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv'
df = pd.read_csv(data_url)

df.shape # Hide 

df.columns # Hide

df.describe() # Hide

df.info() # Hide

df.head() # Hide

with open(f'{argv[0]}.html', 'w') as file:                 # Hide
    file.write(df.describe().to_html())                        # Hide
    file.write(df.head().to_html())                        # Hide

ASEAN_countries = ['Brunei', 'Burma', 'Cambodia',    'Indonesia', 'Laos', 'Malaysia',    'Philippines', 'Singapore', 'Vietnam'] # Hide

filtered_ASEAN_rows = df['Country'].isin(ASEAN_countries) 

df_ASEAN = df[filtered_ASEAN_rows]                     


fig, ax = plt.subplots(figsize=(8, 5)) # Hide

# Pandas Manipulation #
latest_date = max(df_ASEAN['Date'])
df_ASEAN_latest_date = df_ASEAN[df_ASEAN['Date'] == latest_date]
#df_ASEAN_latest_date.set_index('Country', inplace = True)
#df_ASEAN_latest_date.sort_values(by = 'Deaths', ascending=True, inplace = True)

# Plotting #
ax = df_ASEAN_latest_date['Deaths'].plot(kind = 'bar')

# Pretty Things #
ax.set_xlabel('Country', fontsize = 12)
ax.set_ylabel('Total Death by Countries', fontsize = 12)
ax.set_title('Number of Deaths due to COVID-19 by countries', fontsize = 15)
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)
plt.tight_layout()
plt.savefig(f'{argv[0]}.png')  # Hide
plt.show()
