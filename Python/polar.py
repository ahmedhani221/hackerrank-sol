# Problem: Polar Coordinates

import cmath

z = complex(input())

r = pow(pow(z.real, 2) + pow(z.imag, 2), 0.5)
ph = cmath.phase(z)

print(f"{r:0.3f}")
print(f"{ph:0.3f}")