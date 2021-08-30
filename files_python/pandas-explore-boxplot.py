# %% Result

# %% Things to take note
'''
1. Loading in the dataset from https://raw.githubusercontent.com/nus-sps/workshops.tfi.data-visualisation/main/files/height-weight-metric.csv
2. Note the use of `df.boxplot` for boxplot instead of `df.plot`.
3. For our purposes `plt.suptitle('')` was used 
to remove the secondary title of our boxplot.
'''

# %% Example
import pandas as pd
from sys import argv  # Hide
import matplotlib.pyplot as plt

# Reading in the dataset as df
link = 'https://raw.githubusercontent.com/nus-sps/workshops.tfi.data-visualisation/main/files/height-weight-metric.csv'
df = pd.read_csv(link)

plt.figure(figsize=(5, 5)) # Hide

#Plotting boxplot
ax = df.boxplot('Height', by='Gender')
ax.grid(False)

# Don't forget to add the labels for clarity!
plt.suptitle('')
plt.title('Boxplot of Height (cm) grouped by Gender')
plt.ylabel('Height (cm)')
plt.xlabel('Gender')
plt.tight_layout()
plt.savefig(f'{argv[0]}.png')  # Hide
plt.show()

