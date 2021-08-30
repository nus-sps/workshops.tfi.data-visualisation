# %% Result (Grouping)

# %% Things to take note
'''
1. Loading in the dataset from https://raw.githubusercontent.com/nus-sps/workshops.tfi.data-visualisation/main/files/height-weight-metric.csv
'''

# %% Example (No Grouping)
import pandas as pd
from sys import argv  # Hide
import matplotlib.pyplot as plt

# Reading in the dataset as df
link = 'https://raw.githubusercontent.com/nus-sps/workshops.tfi.data-visualisation/main/files/height-weight-metric.csv'
df = pd.read_csv(link)

plt.figure(figsize=(5, 5)) # Hide

df.plot("Height", 'Weight', kind='scatter')

# Label your axis
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Weight (kg) vs Height (cm)')
plt.tight_layout()
plt.legend()
plt.show()

# %% Example (Grouped)
import pandas as pd
from sys import argv  # Hide
import matplotlib.pyplot as plt

# Reading in the dataset as df
link = 'https://raw.githubusercontent.com/nus-sps/workshops.tfi.data-visualisation/main/files/height-weight-metric.csv'
df = pd.read_csv(link)

plt.figure(figsize=(5, 5)) # Hide

df_grouped_gender = df.groupby("Gender")

fig, ax = plt.subplots()

for name, gender in df_grouped_gender:
    ax.scatter(gender["Height"], gender["Weight"], label=name)

# Label your axis
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Weight (kg) vs Height (cm) grouped by Gender')
plt.tight_layout()
plt.legend()
plt.savefig(f'{argv[0]}.png')  # Hide
plt.show()
