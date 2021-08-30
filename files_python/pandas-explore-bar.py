# %% Result

# %% Things to take note
'''
1. Loading in the dataset from https://raw.githubusercontent.com/nus-sps/workshops.tfi.data-visualisation/main/files/height-weight-metric.csv
2. Standard Error is calculated ourselves.
3. Usage of `groupby`, `.agg` and `yerr`.
'''

# %% Example
import pandas as pd
from sys import argv  # Hide
import matplotlib.pyplot as plt
import numpy as np

# Reading in the dataset as df
link = 'https://raw.githubusercontent.com/nus-sps/workshops.tfi.data-visualisation/main/files/height-weight-metric.csv'
df = pd.read_csv(link)

# Creating a function to calculate standard error
def se(data):
    return np.std(data) / np.sqrt(data.count())

df_height_grouped = df.groupby("Gender")['Height']

plt.figure(figsize=(5, 5)) # Hide

df_height_mean_se_gender = df_height_grouped.agg([np.mean, se])
df_height_mean_se_gender.plot(kind = 'bar', yerr = 'se',capsize=10, rot=0)

plt.ylabel('Average Height (cm)')
plt.xlabel('Gender')
plt.title('Average Height (cm) vs Gender')
plt.legend().remove
plt.tight_layout()
plt.savefig(f'{argv[0]}.png')  # Hide
plt.show()

