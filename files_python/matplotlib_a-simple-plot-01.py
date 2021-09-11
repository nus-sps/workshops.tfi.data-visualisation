# %% Results

# %% Code
'''
- You can have only a <code>scatter</code> (without error bars) by using scatter (which is commented below).
- <code>fmt</code> is short for ‘format string’. This decides the shape of the data point.
- The \$…\$ allows us to use (a limited set of) LaTeX commands!
'''

from sys import argv  # Hide

from matplotlib import pyplot as plt

# Some data for plotting
x = [0, 1, 2, 3, 4, 5]
y_1 = [0, 2, 4, 6, 8, 10]
y_2 = [0, 4, 8, 12, 16, 20]
err = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5]

# Lets start plotting
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(5, 5))
ax.plot(x, y_1, color='red', linestyle='dashed', label='$Y_1$ values')
ax.errorbar(x, y_2, yerr=err, xerr=.25, color='black', fmt='o', label='$Y_2$ values')
# ax.scatter(x, y_2, color='blue', label='$Y_2$ values')

ax.set_xlabel('x-values')
ax.set_ylabel('y-values')
ax.set_title('X vs Y')
ax.grid(alpha=.25)
ax.legend(loc='upper left')
plt.savefig(f'{argv[0]}.png', dpi=150)  # Hide
plt.show()
