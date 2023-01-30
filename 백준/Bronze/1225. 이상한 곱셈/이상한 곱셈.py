import sys
a,b = map(list, sys.stdin.readline().split())
cnt_a = 0
cnt_b = 0
for i in a :
    cnt_a +=(int(i))
for j in b :
    cnt_b +=(int(j))
print(cnt_a * cnt_b)