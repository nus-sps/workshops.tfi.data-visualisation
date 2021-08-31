# %% Result

# %% Tasks
'''
Assuming we are only interested in Number of Deaths and Number of Confirmed cases.

1. What are all the columns in the this dataset.
2. **Drop** unnecessary columns.
3. **Keep** necessary columns
'''

# %% Solution (Drop Columns)
import pandas as pd  # Hide
from sys import argv  # Hide

data_url = 'https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv' # Hide
df = pd.read_csv(data_url) # Hide

df_dropped = df.drop(columns = 'Recovered')
df_dropped.head()

with open(f'{argv[0]}.html', 'w') as file:                 # Hide
    file.write(df_dropped.head().to_html())                  # Hide


# %% Solution (Keep Columns)
import pandas as pd  # Hide
from sys import argv  # Hide

data_url = 'https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv' # Hide
df = pd.read_csv(data_url) # Hide

df_keep = df[["Date", "Country", "Confirmed", "Deaths"]]
df_keep.head()
