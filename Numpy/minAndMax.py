# Problem: Min and Max

import numpy as np

N, M = map(int, input().split())

arr = np.array([list(map(int, input().split())) for i in range(N)])

min = np.min(arr,  axis = 1)
print(np.max(min))
