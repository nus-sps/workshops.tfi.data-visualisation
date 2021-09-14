import numpy as np
import pandas as pd

df = pd.read_excel('./files/dummy_class.xls')

link = 'https://raw.githubusercontent.com/nus-sps/workshops.tfi.data-visualisation/main/files/dummy_class.xls'

pd.read_excel(link)

df.head(3)
df.tail(3)
df.shape
len(df)
df.columns
df.index
df.describe()       # For numbered columns
df.info()

df['Major'].value_counts().plot(kind='barh')       # For all columns

df['Major'].unique()
'''
Lets ask some questions:
1. How many rows and colums are there?
    - `df.shape`
1. What are the names of the columns?
1. Can we look at the data?
'''


# Locating missing dataset

df.fillna(0, inplace=True)

df.isin(['Maryjane Sandoval']).any()

df['Major'].size()

# %%
df = pd.read_excel('files/dummy_class.xls')
df.drop(columns=['Unnamed: 0'], inplace=True)
students = ['Maryjane Sandoval', 'Ronin Christian']
mask = df.isin(students).any(axis=1)
df[mask]
mask

df.columns
