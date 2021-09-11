
# %% Results

# %% Tasks
'''
1. Reproduce the plot of Example 1 in Colab by copying and pasting the code.

2. Comment the <code>errorbar</code> plot to and un-comment the <code>scatter</code> plot.

2. Visit <a href="https://colorbrewer2.org/" target="_blank">colorbrewer2.org</a> and select two qualitative colour that is colourblind friendly and print friendly.

3. Change the following properties of the plot.

   1. Change colour of the line to **your first colour**.
   1. Change colour of the scatter to **your second colour**.
   2. Change the title to ‘**X vs. Y and 2Y**’

4. Change the colour of the grid to **gray**.

5. Change the format of the saved figure to PDF.

6. Download the saved plot into your computer.

   Please spend not more that **5 minutes** on this exercise.
'''
# %% A Solution


from sys import argv  # Hide

from matplotlib import pyplot as plt

# Some data for plotting
x = [0, 1, 2, 3, 4, 5]
y_1 = [0, 2, 4, 6, 8, 10]
y_2 = [0, 4, 8, 12, 16, 20]
err = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5]

# Lets start plotting
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(5, 5))
ax.plot(x, y_1, color='#7570b3', linestyle='dashed', label='$Y_1$ values')
ax.scatter(x, y_2, color='#d95f02', label='$Y_2$ values')

ax.set_xlabel('x-values')
ax.set_ylabel('y-values')
ax.set_title('X vs Y and 2Y')
ax.grid(alpha=.25, color='gray')
ax.legend(loc='upper left')

plt.savefig(f'{argv[0]}.png', dpi=150)  # Hide
plt.savefig('simple-01.png', dpi=150)
plt.show()
