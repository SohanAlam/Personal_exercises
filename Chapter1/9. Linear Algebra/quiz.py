import sympy as sympy
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn


c_list = [1,2]
#print("The list:",c_list)
#print("Has length:", len(c_list))

c_vector = np.array(c_list)
#print("The vector:", c_vector)
#print("Has shape:",c_vector.shape)

A = np.arange(6).reshape((3,2))
C = np.random.randn(2,2)

print( A.shape)
print( C.shape)

