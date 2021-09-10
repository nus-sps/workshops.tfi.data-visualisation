# %% Exercise

from sys import argv  # Hide

from matplotlib import pyplot as plt

# Some data for X and Y Datasets
X = [-1, -2, 0, 2, 1]
Y = [1, 2, 0, -2, -1]
# Building on the same plot
#plt.plot(X,Y,color='red', marker='o',mfc='black')
plt.plot(X, Y, color='red', marker='o', mfc='black')  # Hide

# Add x_labels, y_labels and Title
plt.xlabel('x-axis')  # Hide
plt.ylabel('y-axis')  # Hide
plt.title('title')  # Hide
# plt.   ()
# plt.   ()
# plt.   ()
# Next we would need to showcase the plot generated.
plt.show()
plt.savefig(f'{argv[0]}.png', dpi=100)  # Hide

# %% Results

# %% Solution
# Some data for X and Y Datasets
X = [-1, -2, 0, 2, 1]
Y = [1, 2, 0, -2, -1]
# Building on the same plot
plt.plot(X, Y, color='red', marker='o', mfc='black')
# Add x_labels, y_labels and Title
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('title')
# Next we would need to showcase the plot generated.
plt.savefig(f'{argv[0]}.png', dpi=100)  # Hide
plt.show()
