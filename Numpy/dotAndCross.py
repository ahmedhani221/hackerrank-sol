# Problem: Dot and Cross

import numpy as np

N = int(input())

A = [list(map(int, input().split())) for i in range(N)]
B = [list(map(int, input().split())) for i in range(N)]

A = np.array(A)
B = np.array(B)

res = np.dot(A, B)

print(res)