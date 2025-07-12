#Problem: Symmetric Difference

m = int(input())
a = set(map(int, input().split()))

n = int(input())
b = set(map(int, input().split()))

diff1 = a.difference(b)
diff2 = b.difference(a)
symm = list(diff1.union(diff2))

symm.sort()

for i in symm:
    print(i)


