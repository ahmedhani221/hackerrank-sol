# Problem: Zeros and Ones

import numpy as np

dim = tuple(map(int, input().split()))  # I did it this way cuz I noticed zeros and ones functions take the dimensions as a tuple

print(np.zeros(dim, dtype = int))
print(np.ones(dim, dtype = int))
