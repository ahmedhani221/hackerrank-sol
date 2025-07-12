# Problem: Set .add()

countries = set()

n = int(input())

for i in range(n):
    s = input()
    countries.add(s)
    
print(len(countries))
