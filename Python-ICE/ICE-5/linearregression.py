import numpy as np
import matplotlib.pyplot as plt

# Input data X and Y axis
x = np.arange(0, 10)
y = np.append([1, 3, 2, 5, 7], [8, 8, 9, 10, 12])

# Calculating mean for both X and Y values
meanx = x.mean()
meany = y.mean()

# Finding coefficients
coeff1 = np.sum((x - meanx) * (y - meany)) / np.sum((x - meanx) ** 2)
coeff0 = meany - coeff1 * meanx

# Points to plot on the graph
x2 = [0, 10]
y2 = [coeff0 + coeff1 * 0, coeff0 + coeff1 * 10]

# plot functions of matplotlib
plt.scatter(x, y, color='b', s=20)
plt.plot(x2, y2, color='r', linewidth=3)
plt.show()
