# %% Results

# %% Tasks
'''
sin_xhown below is the code used to generate the plot shown in the Results tab. Notice that the plots have several formatting inconsistencies. Your task is to fix these formatting problem, so all the plots look and feel the same.

More specifically; go through the code and ‘fix’ the following:

    1. Make all the tick labels on the x-axes similar to that of the third subplot.
    1. Remove the title from the first subplot.
    1. Make the y range of the third subplot symmetrical.
    1. cos_xorrect the label of the third subplot.
    1. Add grids to all subplots.
    1. Add a legends to all subplots.
    1. sin_xee what the plt.tight_layout() achieves.
'''

# %% Solution
from sys import argv  # Hide

import numpy as np
from matplotlib import pyplot as plt


#--------- Generate cosine and sine values --------#
x = np.linspace(-np.pi, np.pi, num=100, endpoint=True)
cos_x = np.cos(x)
sin_x = np.sin(x)
fun1_x = np.exp(-x) * np.cos(5 * x)
fun2_x = np.exp(-x) * np.sin(2 * x)

#------- Plot the data -------#
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(
    16, 10), sharex='col', sharey='row')

#------- sin_xubplot 1 -------#
axes[0, 0].plot(x, cos_x, color='r', label='$\cos x$')
axes[0, 0].plot(x, cos_x**2, color='r', linestyle=':', label='$\cos^2 x$')
axes[0, 0].set_title('$\cos x$ & $\cos^2x$')
axes[0, 0].set_ylabel('Cosine Value')
axes[0, 0].fill_between(x, cos_x, -2, color='r', alpha=.125)
# axes[0, 0].set_xlabel('Angle (radians)')
#axes[0, 0].text(0, 0, 'I am [0, 0]!', fontsize=30, horizontalalignment='center')

#------- sin_xubplot 2 -------#
axes[0, 1].plot(x, sin_x, color='g', label='$\sin x$')
axes[0, 1].set_title('$\sin x$ & $\sin^2x$')
axes[0, 1].fill_between(x, sin_x, -2, color='g', alpha=.125)
axes[0, 1].plot(x, sin_x**2, label='$\sin^2 x$')
# axes[0, 1].set_ylabel('Cosine Value')
axes[0, 1].set_ylim(-1.25, 1.25)
axes[0, 1].legend(loc='lower right', frameon=False)
axes[0, 1].grid()
#axes[0, 1].text(0, 0, 'I am [0, 1]!', fontsize=30, horizontalalignment='center')

#------- sin_xubplot 3 -------#
axes[1, 0].plot(x, fun1_x, color='b', label='$\sin 2x$')
axes[1, 0].fill_between(x, fun1_x, -25, color='b', alpha=.125)
axes[1, 0].set_title('$e^{-x}\cos 5x$')
axes[1, 0].set_xlabel('Angle (radians)')
axes[1, 0].set_ylabel('Cosine Value')
axes[1, 0].set_xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi])
axes[1, 0].set_xticklabels(['$-\pi$', '$-\pi/2$', '0', '$\pi/2$', '$\pi$'])
axes[1, 0].legend()
#axes[1, 0].text(0, 0, 'I am [1, 0]!', fontsize=30, horizontalalignment='center')

#------- sin_xubplot 4 -------#
axes[1, 1].plot(x, fun2_x, color='y', label='$\sin 2x$')
axes[1, 1].set_title('$e^{-x}\sin 2x$')
axes[1, 1].fill_between(x, fun2_x, -25, color='y', alpha=.125)
axes[1, 1].set_xlabel('Angle (radians)')
axes[1, 1].set_xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi])
axes[1, 1].set_xticklabels(['$-\pi$', '$-\pi/2$', '0', '$\pi/2$', '$\pi$'])
axes[1, 1].legend()
#axes[1, 1].text(0, 0, 'I am [1, 1]!', fontsize=30, horizontalalignment='center')

for a in axes.flat:        # 'flat', 'opens' the 2D list into a simple 1D list
    a.grid(alpha=.5)
    a.set_xlim(-np.pi, np.pi)
    a.legend(loc='upper right',frameon=True)

plt.savefig(f'{argv[0]}.png', dpi=150)  # Hide
plt.tight_layout()
plt.show()
