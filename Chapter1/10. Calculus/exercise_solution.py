import matplotlib.pyplot as plt
from scipy.misc import derivative
import numpy as np

#1. Plot the absolute value of x and its derivative. Choose an interval to have a nice looking shape.

def sin(x):
    return np.sin(x)
derivative(sin, np.pi, dx=1e-6)
x = np.linspace(0,2*np.pi, 1000)
plt.plot(x, sin(x))
plt.show()

#2. Plot the function $x\log(x)$ and its derivative.
def function(x):
    return x / np.log(x)
def deriv(x):
    return derivative(function, x)
x = np.linspace(-50,100)
y = x / np.log(x)
plt.plot(x,deriv(y))
plt.show()

3. Plot the function $e^{x}\log(x)+5$ and its derivative.


def function(x):
    return e^{x} / np.log(x)+5
def deriv(x):
    return derivative(function, x)
x = np.linspace(-50,100)
y = (np.log)**(-1)*(x) / np.log(x)+5
plt.plot(x,deriv(y))
plt.show()









