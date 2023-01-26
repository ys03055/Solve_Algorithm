from collections import deque

n = int(input())
s = deque()
result = []
for i in range(1,n+1) :
    s.append(i)

while len(s) != 1 :
    result.append(s[0])
    s.popleft()
    s.append(s.popleft())
result.append(s[0])
print(*result)