import numpy as np
def add_vectors():

    u = np.array([1,2,3,4,5])
    v =np.array([9,8,7,6,5])
    x =np.add(u,v)
    print(x)

add_vectors()

def scalar_mult():
  s = 5
  v = np.array([2,3,4,5])
  x1 = np.multiply(s,v)
  print(x1)

scalar_mult()

def dot_product():
  p = np.array([2,4,6,8])
  q = np.array([1,3,5,7])
  r = np.sum([p,q])
  print(r)

dot_product()
