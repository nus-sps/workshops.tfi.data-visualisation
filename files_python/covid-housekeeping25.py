# %% Tasks
'''
Assuming we are only interested in Number of Deaths and Number of Confirmed cases.

1. What are all the columns in the this dataset.
2. **Keep** all necessary columns.
'''

# %% Another Solution
import pandas as pd  # Hide
from sys import argv  # Hide

data_url = 'https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv' # Hide
df = pd.read_csv(data_url) # Hide

df_keep = df[["Date", "Country", "Confirmed", "Deaths"]]
df_keep.head()

with open(f'{argv[0]}.html', 'w') as file:                 # Hide
    file.write(df_keep.head().to_html())                  # Hide
