import numpy as np

import math

def mag():
    v = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    magnitude = np.linalg.norm(v)
    print(magnitude)

mag()

def mag_dir():
    v1 = np.array([5,1])
    v2 = np.array([-4,-1])
    vec = v1 + v2
    mag = np.linalg.norm(vec)
    print("magnitude:", mag)
    l1 = v1 / np.linalg.norm(v1)
    l2 = v2 / np.linalg.norm(v2)
    dot_product = np.dot(l1, l2)
    angle = np.arccos(dot_product)
    degrees = math.degrees(angle)
    print("Direction:", degrees)

mag_dir()


