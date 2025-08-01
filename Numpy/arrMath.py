# Problem: Array Mathematics

import numpy as np

N, M = map(int, input().split())

A = np.array([list(map(int, input().split())) for i in range(N)])
B = np.array([list(map(int, input().split())) for i in range(N)])

print(np.array(A + B))
print(np.array(A - B))
print(np.array(A * B))
print(np.array(A // B))
print(np.array(A % B))
print(np.array(A ** B))

