

from numpy import array

array1 = [1,1,3,5,15]
def task1(array1):
    for num in array1:
        if (num % 3 == 0)  and  (num % 5==0):
            print( "strive School ")
        elif num % 3 == 0:
            print( "Strive")
        elif num % 5 == 0:
            print( "School ")
        else:
            print(num)
task1(array1)