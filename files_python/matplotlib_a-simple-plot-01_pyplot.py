# %% Results

# %% Code
'''
- `matplotlib` allows several syntaxes. One is referred to as the **pyplot API**. It is simple but can be limited.
-The version we are using is referred to as the **object-oriented API**.
It is slightly complicated but offers more flexibility and versatility than the pyplot API.
- Just for comparison, here is the code using pyplot API format
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
plt.savefig(f'{argv[0]}.png', dpi=100)  # Hide
plt.show()
