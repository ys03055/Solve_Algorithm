import sys
n = int(sys.stdin.readline())
s = []
for i in range(n) :
    a = int(sys.stdin.readline())
    s.append(a)
s1 =list(reversed(s))
cnt = 1
max = s1[0]
for i in s1 :
    if max < i :
        max = i
        cnt +=1
print(cnt)