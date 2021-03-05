# import packages
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import Random class
from random import Random

# instantiate Random class with seed
random = Random(5555)

# variables for our region of interest
Xmin = -75
Xmax = 150


# define flat distribution scaled to cos(x) max
def Flat(x):
    return 0.01

# sample from a flat distribution
def SampleFlat():
    return Xmin + (Xmax-Xmin)*random.rand()

# normal distribution function
def normal(x, mean, sd):
    return (1/np.sqrt(2*np.pi*sd**2)*np.exp(-0.5*((x-mean)/sd)**2))

# target distribution
def target(x):
    return (normal(x,20,30)+normal(x,75,25))/2


# get user input for number of trials
p0 = sys.argv.index("-Ntrial")
trials = int(sys.argv[p0+1])

# loop through trials, generate random number from trial distribution,
# check to see whether it is accepted or rejected
# if accepted, appended to approximation array
approx = []
for i in range(0,trials):
    X = SampleFlat()
    R = target(X)/Flat(X)
    rand = random.rand()
    if (rand <= R):
        approx.append(X)

# define the x-range
x = np.linspace(-75,150,1000)
    
# more plot stuff
fig, ax = plt.subplots(figsize = (6,6))
ax.plot(x, target(x), color="forestgreen", label="Target")
ax.hist(approx, label="Approximation", density=True)
ax.axhline(0.01,-75,150, color="firebrick", label="Proposal")
ax.set_title("Rejection Hurts")
ax.set_xlabel("x")
ax.set_ylabel("Probability")
ax.set_xlim([-75,150])
ax.set_ylim([0,0.015])
ax.legend()
ax.grid(True)

plt.show()
