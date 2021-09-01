# %% Result

# %% Code
'''
- We generate two sets of data sin x and cos x
- We want to plot these two graphs side by side but do not want them to be on
the same figure!
- This is done using the `plt.subplots()` argument.
- `plt.subplots()` also has `ncols = ` to specify the number of columns!
'''

from sys import argv  # Hide
from matplotlib import pyplot as plt
import numpy as np

# Generating data
x = np.linspace(-np.pi, np.pi, num=30, endpoint=True)
cos_x = np.cos(x)
sin_x = np.sin(x)


# Specify how many columns or rows
fig, ax = plt.subplots(nrows = 2, figsize=(6, 5), sharex = True)

ax[1].set_xlabel('x-axis!', fontsize = 12)

# Aesthetics & Plotting for ax[0] #
ax[0].plot(x, sin_x, marker = 'o', linestyle = '-' ,label='sin x')
ax[0].hlines(0, xmin = -np.pi, xmax = np.pi, linestyle = 'dashed')
ax[0].set_ylabel('y-axis for sin x!',fontsize = 12)
ax[0].set_title('title for sin x!',fontsize = 15)


# Aesthetics & Plotting for ax[1] #
ax[1].plot(x, cos_x, label='cos x', color='green')
ax[1].hlines(0, xmin = -np.pi, xmax = np.pi, linestyle = 'dashed')
ax[1].set_ylabel('y-axis for cos x!',fontsize = 12)
ax[1].set_title('title for cos x!',fontsize = 15)

for axes in ax.flat:
     axes.legend(loc='upper left', frameon=False)
     axes.grid(axis='x', alpha=.5)


plt.tight_layout()
plt.savefig(f'{argv[0]}.png')  # Hide
plt.show()

