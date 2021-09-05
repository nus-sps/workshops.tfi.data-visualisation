# %% Result

# %% Code
'''
- We generate a set of data that are Normally distributed
- We used `plt.boxplot()` to generate the boxplot!
- Here we used another package,numpy to create a separate array
'''

from sys import argv  # Hide
from matplotlib import pyplot as plt
import numpy as np


# Some data for plotting
data = [0,0,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,5,5,6,7,7,8,8,9,10]
data1 = np.array(data) / 1.5 * 5
print(data1)

fig, ax = plt.subplots(figsize=(6, 5)) # Hide

# Actual plotting #
ax.boxplot([data, data1], labels = ['data','data1']) # Hide
plt.boxplot([data, data1], labels = ['data','data1'])


# Aesthetics #
plt.xlabel('This is the x-axis', fontsize = 16)
plt.ylabel('This is the y-axis', fontsize = 16)
plt.title('This is the Title!', fontsize = 20)
plt.tight_layout()
plt.savefig(f'{argv[0]}.png')  # Hide
plt.show()

