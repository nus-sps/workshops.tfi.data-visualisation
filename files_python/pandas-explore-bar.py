# %% Result

# %% Things to take note
'''
1. Loading in the dataset from https://raw.githubusercontent.com/nus-sps/workshops.tfi.data-visualisation/main/files/height-weight-metric.csv
2. Standard Deviation and Mean are calculated using numpy.
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

df_height_grouped = df.groupby("Gender")['Height']

plt.figure(figsize=(5, 5)) # Hide

df_height_mean_se_gender = df_height_grouped.agg([np.mean, np.std])
df_height_mean_se_gender.plot(kind = 'bar', yerr = 'std',capsize=10, rot=0,legend=False)

plt.ylabel('Average Height (cm)')
plt.xlabel('Gender')
plt.title('Average Height (cm) vs Gender')
plt.tight_layout()
plt.savefig(f'{argv[0]}.png')  # Hide
plt.show()

