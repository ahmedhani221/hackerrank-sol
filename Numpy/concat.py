# Problem: Concatenate

import numpy as np

N, M, P = map(int, input().split())

arr1 = [list(map(int, input().split())) for i in range(N)]
arr2 = [list(map(int, input().split())) for i in range(M)]
arr1 = np.array(arr1)
arr2 = np.array(arr2)

res = np.concatenate((arr1, arr2), axis=0)
print(res)