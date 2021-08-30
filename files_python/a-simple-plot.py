# %% Results

# %% Code
'''
- You can have only a `scatter` (without error bars) by using scatter (which is commented below).
- `fmt` is short for ‘format string’. This decides the shape of the data point.
- The $…$ allows us to use (a limited set of) LaTeX commands!
'''

from sys import argv  # Hide

from matplotlib import pyplot as plt

# Some data for plotting
x = [0, 1, 2, 3, 4, 5]
y_1 = [0, 2, 4, 6, 8, 10]
y_2 = [0, 4, 8, 12, 16, 20]
err = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5]

# Lets start plotting
plt.figure(figsize=(5, 5))
plt.plot(x, y_1, color='red', linestyle='dashed', label='$Y_1$ values')
plt.errorbar(x, y_2, yerr=err, color='black', fmt='o', label='$Y_2$ values')

plt.xlabel('x-values')
plt.ylabel('y-values')
plt.title('X vs Y')
plt.grid(alpha=.25)
plt.legend(loc='upper left')
plt.savefig(f'{argv[0]}.png', dpi=150)  # Hide
plt.show()