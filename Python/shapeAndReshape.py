# Problem: Shape and Reshape

import numpy as np

arr = input().strip().split(' ')

arr = np.array(arr, dtype='i')
arr = arr.reshape(3, 3)

print(arr)
