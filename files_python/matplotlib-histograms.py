# %% Result

# %% Code
'''
- We generate a set of data that are Continously distributed
- We used `plt.hist()` to generate the histogram!
'''

from sys import argv  # Hide
from matplotlib import pyplot as plt

# Some data for plotting
data = [0,0,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,5,5,6,7,7,8,8,9,10]



fig, ax = plt.subplots(figsize=(6, 5)) # Hide

# Actual plotting #
plt.hist(data, bins = 10,color='#C0C0C0')

# Aesthetics #
plt.xlabel('This is the x-axis', fontsize =8)
plt.ylabel('This is the y-axis', fontsize = 12)
plt.title('This is the Title!', fontsize = 16)
plt.tight_layout()
plt.savefig(f'{argv[0]}.png')  # Hide
plt.show()

