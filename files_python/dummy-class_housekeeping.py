# %% Result

# %% Tasks
'''
```python
import pandas as pd
df = pd.read_excel('dummy_class.xls')
```

  Starting with the code above, answer the questions in the following table using the Pandas command indicated.

|      | Question                                        |          Possible code           |
| :--: | ----------------------------------------------- | :------------------------------: |
|  1.  | How many rows and columns are there?            |            `df.shape`            |
|  2.  | What are the names of the columns?              |           `df.colmns`            |
|  3.  | Can we look at a sample of the data             |   `df.head()`<br />`df.tail()`   |
|  4.  | What type of data is contained?                 |           `df.info()`            |
|  5.  | Can we have descriptive statistics of the data? |         `df.describe()`          |
|  6.  | What are the unique values in a column?         |    `df[column_name].unique()`    |
|  7.  | How many unique values are there?               | `df[column_name].value_counts()` |


'''

# %% Solution
from sys import argv  # Hide

import pandas as pd
# df = pd.read_excel('dummy_class.xls')
df = pd.read_excel('files/dummy_class.xls')  # Hide

with open(f'{argv[0]}.html', 'w') as file:            # Hide
    file.write(df.head(10).to_html())                  # Hide

print(f'{argv[0]}.html')

df.shape

df.columns

df.head(3)
df.tail(3)

df.info()

df.describe()

df['Major'].unique()

df['Major'].value_counts()
