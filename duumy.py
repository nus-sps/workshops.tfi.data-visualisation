import numpy as np
import pandas as pd

link = 'https://raw.githubusercontent.com/nus-sps/workshops.tfi.data-visualisation/main/files/dummy_class.xls'

df = pd.read_excel(link)
my_to_replace = {
    'PHY': 'Physics',
    'CHM': 'Chemistry',
    'LS': 'Life Sciences',
    'CBIO': 'Comp. Biology',
    'F': 'Female',
    'M': 'Male'
}

df.replace(to_replace=my_to_replace, inplace=True)
my_to_drop = 'Unnamed: 0'
df.drop(columns=my_to_drop, inplace=True)
df.fillna(0, inplace=True)
df['Total (100%)'] = df['Test 1 (30%)'] +	df['Test 2 (20%)'] +	df['Test 3 (50%)']
mask = (df['Major'] == 'Physics') & (df['Total (100%)'] <= 60)
df[mask].to_html()

df.groupby(by='Major').agg(['count',np.mean, np.std])
