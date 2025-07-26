# Problem: Mean, Var, and Std

import numpy as np

N, M = map(int, input().split())

arr = np.array([list(map(int, input().split())) for i in range(N)])

print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(round(np.std(arr), 11))
