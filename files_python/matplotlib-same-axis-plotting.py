# %% Result

# %% Code
'''
- We generate two sets of data `data_1` and `data_2`
- Note the use of `marker`, `linestyle`, `color` and `label`!
- Note that both graphs are plotted on the same figure!
- If you would like a scatterplot with no lines, try `plt.scatter()`!
'''

from sys import argv  # Hide
from matplotlib import pyplot as plt

# Some data for plotting
x_1 = [0, 1, 2, 3, 4, 5]
y_1 = [0, 2, 4, 6, 8, 10]

x_2 = [5, 4, 3, 2, 1, 0]
y_2 = [0, 2, 4, 6, 8, 10]



fig, ax = plt.subplots(figsize=(6, 5)) # Hide

# Actual plotting #
plt.plot(x_1, y_1, marker = 'o', linestyle = '-', 
          color = '#08D9D6', label = 'Graph 1')

plt.plot(x_2, y_2, marker = '*', markersize='5', linestyle = 'dashed',
          color = '#FF2E63', label = 'Graph 2')

# Aesthetics #
plt.legend()
plt.xlabel('This is the x-axis', fontsize = 16)
plt.ylabel('This is the y-axis', fontsize = 16)
plt.title('This is the Title!', fontsize = 20)
plt.tight_layout()
plt.savefig(f'{argv[0]}.png')  # Hide
plt.show()

