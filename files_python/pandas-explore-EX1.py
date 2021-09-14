# %% Result

# %% Tasks
'''
1. Loading in the dataset from https://raw.githubusercontent.com/nus-sps/workshops.tfi.data-visualisation/darren-branch/files/StudentPerformance2.csv
2. What is the shape of the data? I.e how many rows and columns are there?
3. What does the dataframe look like?
4. Drop unnecessary columns that might not affect test scores
'''

# %% Solution
import pandas as pd
from sys import argv  # Hide

# Reading in the dataset as df
link = 'https://raw.githubusercontent.com/nus-sps/workshops.tfi.data-visualisation/darren-branch/files/StudentPerformance2.csv'
df = pd.read_csv(link)

df.shape

df.head()

df_dropped = df.drop(columns = ['lunch', 'gender'])
df_dropped.head()
with open(f'{argv[0]}.html', 'w') as file:                 # Hide                     # Hide
    file.write(df.head().to_html())                        # Hide
    file.write(df_dropped.head().to_html())                        # Hide

