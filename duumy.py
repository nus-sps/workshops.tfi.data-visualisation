import numpy as np
import pandas as pd

df = pd.read_excel('./files/dummy_class.xls')

df.head(3)
df.tail(3)
df.shape
len(df)
df.columns
df.index
df.describe()       # For numbered columns
df.info()           # For all columns

'''
Lets ask some questions:
1.
'''
