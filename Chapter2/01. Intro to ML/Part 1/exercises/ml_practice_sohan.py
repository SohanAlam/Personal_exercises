            #file loading
import csv
import numpy as np
import pandas as pd

file_name = "01. Intro to ML\Part 1\exercises\iris.data"
with open (file_name, 'r') as f:
    data = list(csv.reader(f, delimiter = ','))
data1 = np.array(data)
print(data1.shape)

#another way

#data = np.loadtxt(file_name,delimiter=",")

#print(data.shape)





