# %% Result

# %% Tasks
'''
Let's tidy up our dataset by:

1. Dropping unnecessary columns (i.e.'Unnamed: 0')
2. Replacing the majors with full names:
1. Replacing 'M' and 'F' with thier full form.

  | Before |     After     |
  | :----: | :----------- |
  |  PHY   |    Physics    |
  |  CHM   |   Chemistry   |
  |   LS   | Life Sciences |
  | CBIO'  | Comp. Biology |
'''

# %% Solution
from sys import argv  # Hide

import pandas as pd  # Hide

df = pd.read_excel('./files/dummy_class.xls')  # Hide

my_to_replace = {
    'PHY': 'Physics',
    'CHM': 'Chemistry',
    'LS': 'Life Sciences',
    'CBIO': 'Comp. Biology',
    'F': 'Female',
    'M': 'Male'
}

# What does inplace do?
df.replace(to_replace=my_to_replace, inplace=True)

# Now lets drop the unnecessary columns
my_to_drop = 'Unnamed: 0'
df.drop(columns=my_to_drop, inplace=True)

with open(f'{argv[0]}.html', 'w') as file:             # Hide
    file.write(df.head(10).to_html())                  # Hide
