import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
import matplotlib.cm as cm



from scipy import integrate

a, b = [2, 5]       
def f(x):
    return 5
#f = 5
result = integrate.quad(f, a, b)
result
print(result)

area_under_the_curve = result[0]

x = 5
section = np.arange(2, 5, 1/100)
plt.plot(x, f(x))
plt.fill_between(section,f(section))