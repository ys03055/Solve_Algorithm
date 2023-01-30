import sys
s = []
for i in range(10) :
    a = int(sys.stdin.readline())
    z = a % 42
    if z not in s :
        s.append(z)
print(len(s))