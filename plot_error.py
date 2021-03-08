# import packages
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# error list from Trapezoidal Rule and corresponding
# list containing number of intervals used
# (values obtained from running integrate.py)
trap_error = [1.99581703, 1.11895245, 0.73945501, 0.53531255, 0.41071214, 0.32807609, 0.26994610]
trap_intervals = [2,3,4,5,6,7,8]

# error list from Gaussian Quadrature and corresponding
# list containing number of intervals used
gaus_error = [-0.34821586, -0.14420892, -0.05556518, -0.00711044, 0.02437133, 0.04925224, 0.07841782]
gaus_intervals = [2,3,4,5,6,7,8]

# relative error difference between the two and number of intervals used
error_diff = [2.34403289, 1.26316137, 0.79502019, 0.54242299, 0.38634081, 0.27882386, 0.19152828]
intervals = [2,3,4,5,6,7,8]


# make plots
plt.figure()
plt.plot(trap_intervals, trap_error, label="Trapezoid Error")
plt.plot(gaus_intervals, gaus_error, label="Gaus Quad Error")
plt.plot(intervals, error_diff, label="Error Difference")
plt.title("Error Comparisons", fontweight="bold")
plt.xlabel("Number of Intervals Used")
plt.ylabel("Error from True Value")
plt.legend()

plt.show()
