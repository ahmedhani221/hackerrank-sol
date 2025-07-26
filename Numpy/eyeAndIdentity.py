# Problem: Eye and Identity

import numpy as np
np.set_printoptions(legacy='1.13')

N, M = map(int, input().split())

iden = np.eye(N, M)
print(iden)