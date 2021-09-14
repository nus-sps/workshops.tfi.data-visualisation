# %% Result

# %% Tasks
'''
1. Plot a scatterplot between the three test scores!
2. Use plt.subplots() to have 3 rows of graphs
'''

# %% Solution
import pandas as pd # Hide
from sys import argv  # Hide
import matplotlib.pyplot as plt # Hide

link = 'https://raw.githubusercontent.com/nus-sps/workshops.tfi.data-visualisation/darren-branch/files/StudentPerformance2.csv' # Hide
df = pd.read_csv(link) # Hide
df_dropped = df.drop(columns = ['lunch', 'gender']) # Hide

# Init subplots
fig, ax = plt.subplots(ncols = 3, figsize = (10,5))

# Plotting Reading Score vs Writing
df_dropped.plot("reading.score", "writing.score", kind = 'scatter', ax = ax[0])
ax[0].set_xlabel('reading score')
ax[0].set_ylabel('writing score')
ax[0].set_title('writing vs reading')

df_dropped.plot("reading.score", "math.score", kind = 'scatter', ax = ax[1])
ax[1].set_xlabel('reading score')
ax[1].set_ylabel('math score')
ax[1].set_title('math vs reading')

df_dropped.plot("writing.score", "math.score", kind = 'scatter', ax = ax[2])
ax[2].set_xlabel('writing score')
ax[2].set_ylabel('math score')
ax[2].set_title('math vs writing')

# Don't forget to add the labels for clarity!
plt.tight_layout()
plt.savefig(f'{argv[0]}.png')  # Hide
plt.show()

# %% Interpreting the results
'''
- It seems if a student is struggling with any test, they are bound to struggle for the other tests as well!

- Great! It seems that maybe you could (as a teacher) step in to give students extra guidance if they did not score that well for one test!

- Just remember! This is all ASSOCIATION and not CAUSATION. It just so happens that in these students, if they tend to score badly for one test, they will score badly for the other tests!
'''
