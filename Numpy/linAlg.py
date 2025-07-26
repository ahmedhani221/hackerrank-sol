# Problem: Linear Algebra

import numpy as np

N = int(input())

arr = [list(map(float, input().split())) for i in range(N)]
arr = np.array(arr)

print(round(np.linalg.det(arr), 2))