# %% Results

# %% Code
'''
In this plot:

- We generated sine and cosine graphs.
- We plotted a $y = 0$ line.
- Filled in the spaces where $\cos x > \sin x$ with orange.
- Filled in the spaces where $\sin x > \cos x$ with blue.
'''
from sys import argv  # Hide

import numpy as np
from matplotlib import pyplot as plt

# Generating data
x = np.linspace(-np.pi, np.pi, num=100, endpoint=True)
cos_x = np.cos(x)
sin_x = np.sin(x)

# Plotting
fig, axes = plt.subplots()
axes.plot(x, sin_x, label='sin x')
axes.plot(x, cos_x, label='cos x')
axes.hlines(0, xmin = -np.pi, xmax = np.pi, linestyle = 'dashed')

# Filling
axes.fill_between(x, cos_x, sin_x, where=cos_x > sin_x,
                  color='orange', alpha=.125, label='cos x > sin x')

axes.fill_between(x, cos_x, sin_x, where=cos_x < sin_x,
                  color='b', alpha=.075, label='cos x < sin x')

# Aesthetics
axes.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi]),
axes.set_xticklabels([r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

axes.legend()
axes.grid(axis='x', alpha=.5)

plt.tight_layout()
plt.savefig(f'{argv[0]}.png', dpi=150)  # Hide
plt.show()
