import sys
n = int(sys.stdin.readline())
s = []

for i in range(n) :
    a,b = map(int, sys.stdin.readline().split())
    s.append((a,b))

result = []
for i in range(n) :
    cnt = 0
    for j in range(n) :
        if s[i][0] < s[j][0] and s[i][1] < s[j][1] :
            cnt+=1
    result.append(cnt +1)

for x in result :
    print(x, end=" ")
