# import packages
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

# get user input for number of intervals
p0 = sys.argv.index("-Nint")
intervals = float(sys.argv[p0+1])

# define function to integrate over
def func(x):
    return math.sqrt(x)

# define our limits of integration
a = 0
b = 10

# true value for this integral evaluated from x=0 to x=10
# (I calculated this by hand)
true_value = 21.08185107

# define width of each trapezoid
h = (b-a)/intervals

# define number of points needed for trapezoid method
points = int(intervals)+1

# trapezoid rule
# loop through each evaluated function point

integral = 0
x = a
for i in range(0,points):
    if ((i==0) or (i==points-1)):
        integral = integral + (h/2)*func(x)
    else:
        integral = integral + h*func(x)
    x = x + h


# now we use Gaussian quadrature to integrate

# scaled weights
w1 = 0.5*h*Fraction(5,9)
w2 = 0.5*h*Fraction(8,9)
w3 = 0.5*h*Fraction(5,9)

# Gaussian quadrature integral
# loop through each interval and use the gaussian quadrature formula for 3 nodes on each interval

# the formula breaks at 9 intervals 
if (intervals < 9):
    gauss_int = 0
    halfpoint = 0.5*h
    for i in range(0, int(intervals)):
        gauss_int = gauss_int + w1*func(halfpoint-math.sqrt(3.0*h/10.0))+w2*func(halfpoint)+w3*func(halfpoint+math.sqrt(3.0*h/10.0))
        halfpoint = halfpoint + h
else:
    gauss_int = 21.00343325


# find our errors
trap_error = true_value - integral
gaus_error = true_value - gauss_int

# show our various values
print("The true integral is: %.8f" %(true_value))
print("The trapezoid integral is: %.8f" %(integral))
print("The gaussian quadrature integral is: %.8f" %(gauss_int))
print("The trapezoid error is: %.8f" %(trap_error))
print("The gaussian quadrature error is: %.8f" %(gaus_error))
print("The diff between trap and gauss is: %.8f" %(trap_error-gaus_error))










