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
y_2 = [0, 2, 4, 6, 8, 20]



fig, ax1 = plt.subplots(figsize = (5,5))

# Actual plotting #
ax1.plot(x_1, y_1, marker = 'o', linestyle = '-', 
          color = '#08D9D6', label = 'Graph 1')
ax1.set_xlabel('This is the x-axis', fontsize = 16)
ax1.set_ylabel('This is the y-axis for 1!', fontsize = 16)
ax1.legend()


ax2 = ax1.twinx()  # Create a new Axes object which uses the same x-axis as ax1


ax2.plot(x_2, y_2, marker = '*', markersize='5', linestyle = 'dashed',
          color = '#FF2E63', label = 'Graph 2')
ax2.set_ylabel('This is the y-axis for 2!', fontsize = 16)
ax2.legend()

plt.title('This is the Title!', fontsize = 20)
plt.tight_layout()
plt.savefig(f'{argv[0]}.png')  # Hide
plt.show()

