import numpy as np


def add_matrices():
    m1 = np.matrix([[1,2,3,4],[4,3,2,1]])
    m2 = np.matrix([[9,8,7,6],[6,7,8,9]])
    s = np.sum([m1,m2])
    print(s)

add_matrices()


def scaler():
    sc= 10
    m = np.matrix([[2,4,6,8,],[1,3,5,7]])
    mul =np.multiply(sc,m)
    print(mul)

scaler()

def transpose():
    x = np.matrix([[1,2],[4,5]])
    y = np.transpose(x)
    print(y)

transpose()


