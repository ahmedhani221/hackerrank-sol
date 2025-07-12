# Problem: Transpose and Flatten

import numpy as np

N, M = map(int, input().split())

lst = [list(map(int, input().split())) for i in range(N)]
arr = np.array(lst)

print(arr.transpose())
print(arr.flatten())