# %% Results

# %% Code
from sys import argv  # Hide

from matplotlib import pyplot as plt
import numpy as np

#--------- Generate cosine and sine values --------#
x = np.linspace(-np.pi, np.pi, num=100, endpoint=True)
cos_x = np.cos(x)
sin_x = np.sin(x)
fun_cos_x = np.exp(-x)*np.cos(5*x)
fun_sin_x = np.exp(-x)*np.sin(5*x)

#------------------ Plot the data -----------------#
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8), sharex='col', sharey='row')

# Plot 0,0 : Cosines
axes[0, 0].plot(x, cos_x, color='r', label='cos x')
axes[0, 0].plot(x, cos_x**2, color='grey', linestyle='--', label='cos$^2$ x')
axes[0, 0].set_title('Cosine x & Cosine$^2$ x')
axes[0, 0].set_xlim(-np.pi, np.pi)
axes[0, 0].legend(loc='lower center', frameon=False)

# Plot 0,1 : Sine
axes[0, 1].plot(x, sin_x, color='g', label='sin x')
axes[0, 1].plot(x, sin_x**2, color='grey', linestyle='--', label='sin$^2$ x')
axes[0, 1].set_title('Sin x & Sin$^2$ x')
axes[0, 1].set_ylim(-1.25, 1.25)
axes[0, 1].legend(loc='lower right', frameon=False)

# Plot 1,0 : Function with Cosine
axes[1, 0].plot(x, fun_cos_x, color='r')
axes[1, 0].fill_between(x, fun_cos_x, 0, color='r', alpha=.125)
axes[1, 0].set_title('Function with Cosine')
axes[1, 0].set_xlim(-np.pi, np.pi)

# Plot 0,1 : Function with Sine
axes[1, 1].plot(x, fun_sin_x, color='g')
axes[1, 1].fill_between(x, fun_sin_x, 0, color='g', alpha=.125)
axes[1, 1].set_title('Function with Sine')
axes[1, 1].set_xlim(-np.pi, np.pi)


axes[1, 0].set_xlabel('Angle (radians)')
axes[1, 1].set_xlabel('Angle (radians)')

axes[0, 0].set_ylim(-1, 1)
axes[0, 1].set_ylim(-1, 1)

axes[1, 0].set_ylim(-20, 15)
axes[1, 1].set_ylim(-20, 15)

for a in axes.flat:        # 'flat', 'opens' the 2D list into a simple 1D list
    a.grid(alpha=.5)
    a.set_xlim(-np.pi, np.pi)

plt.tight_layout()
plt.savefig(f'{argv[0]}.png', dpi=150)  # Hide
plt.show()
