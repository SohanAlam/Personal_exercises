import matplotlib.pyplot as plt
from scipy.misc import derivative
import numpy as np

x = np.linspace(-50,50,50)

y= np.cos(-x**9) - np.log(x**6) + np.sin(np.pi*x**2) + np.cos(2* np.pi * x) + np.sqrt(2) / np.pi


#y = np.cos(-x**9) -np.log(x**6) + np.sin(np.pi*x**2) - np.sin(x) + np.cos(np.pi*2*x) + np.sqrt(2)/np.pi

#plt.scatter([0], [-20], c="r")

#plt.plot(x,y)
#plt.grid()
#plt.show()

from scipy.misc import derivative

def sin(x):
    return np.sin(x)
derivative(sin, np.pi, dx=1e-6)
x = np.linspace(0,2*np.pi, 1000)
plt.plot(x, sin(x))
plt.show()





