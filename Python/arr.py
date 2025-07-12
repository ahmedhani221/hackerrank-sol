# Problem: Arrays

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    res = numpy.array(arr, dtype = 'f')
    return res[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)