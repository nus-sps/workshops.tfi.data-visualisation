
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
y_0 = [0,1.5,3,4.5,6,7.5]
y_1 = [0, 2, 4, 6, 8, 10]
y_2 = [0, 4, 8, 12, 16, 20]
err = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5]

# Lets start plotting
plt.figure(figsize=(5, 5))
plt.plot(x,y_0 ,color="#004B63", label='$Y_0$ values')
plt.scatter(x, y_1, color="#30B8B2", linestyle='dashed', label='$Y_1$ values')
plt.errorbar(x, y_2, yerr=err, color="#FF7A4F", fmt='o', label='$Y_2$ values')

plt.xlabel('x-values')
plt.ylabel('y-values')
plt.title('X vs Y')
plt.grid(alpha=.25)
plt.legend(loc='upper left')
plt.savefig(f'{argv[0]}.png', dpi=150)  # Hide
plt.show()
# %% Exercises
'''
- Here we covered how basic plotting works
- Try generating the following graph with black circle markers and Red line
'''

#X and Y Datasets 
X=[-1,0,1]
Y=[1,0,-1]
plt.plot(X,Y,color='red', fmt='bo') # Hide
plt.savefig(f'{argv[0]}.png', dpi=100) # Hide
plt.show()
# %%
from matplotlib import pyplot as plt
import numpy as np
plt.figure(figsize=(5,5))
#plot unit circle
t = np.linspace(0,2*np.pi,101)
plt.plot(np.cos(t),np.sin(t),color='#6A6C6E')

plt.xticks([])
plt.yticks([])

plt.xlabel('Real Values')
plt.ylabel('Imaginary')
plt.title('Complex Roots')
plt.grid(False)
plt.box(False)
#plt.legend(loc='upper left')

plt.show()