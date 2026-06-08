#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
xpoints = np.array([1, 2, 6, 8])
plt.plot(xpoints, ypoints)

plt.savefig("my_plot.png")
print("Chart saved as my_plot.png")
