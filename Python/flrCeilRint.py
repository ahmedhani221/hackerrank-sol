# Problem: Floor, Ceil and Rint

import numpy as np
np.set_printoptions(legacy='1.13')

arr = input().strip().split(' ')

arr = np.array(arr, dtype = 'f')
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))