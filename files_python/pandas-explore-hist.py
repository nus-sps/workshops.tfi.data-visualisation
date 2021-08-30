# %% Result (Grouped)

# %% Things to take note
'''
1. Loading in the dataset from https://raw.githubusercontent.com/nus-sps/workshops.tfi.data-visualisation/main/files/height-weight-metric.csv
2. Usage of `.groupby` to group in histograms
'''

# %% Example (No Grouping)
import pandas as pd
from sys import argv  # Hide
import matplotlib.pyplot as plt
import numpy as np

# Reading in the dataset as df
link = 'https://raw.githubusercontent.com/nus-sps/workshops.tfi.data-visualisation/main/files/height-weight-metric.csv'
df = pd.read_csv(link)

plt.figure(figsize=(5, 5)) # Hide

df['Height'].plot(kind='hist')

# Label your axis
plt.ylabel('Frequency', fontsize = 10)
plt.xlabel('Height (cm)', fontsize = 10)
plt.title('Histogram of Height (cm)', fontsize = 20)
plt.tight_layout()
plt.legend()
plt.show()

# %% Example (Grouped)
import pandas as pd
from sys import argv  # Hide
import matplotlib.pyplot as plt
import numpy as np

# Reading in the dataset as df
link = 'https://raw.githubusercontent.com/nus-sps/workshops.tfi.data-visualisation/main/files/height-weight-metric.csv'
df = pd.read_csv(link)

plt.figure(figsize=(5, 5)) # Hide

grouped_gender = df.groupby("Gender")['Height']
grouped_gender.plot(kind='hist', alpha = 0.5, bins = 15)

# Label your axis
plt.ylabel('Frequency')
plt.xlabel('Height (cm)')
plt.title('Histogram of Height (cm) grouped by Gender')
plt.tight_layout()
plt.legend()
plt.savefig(f'{argv[0]}.png')  # Hide
plt.show()

