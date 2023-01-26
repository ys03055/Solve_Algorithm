t = int(input())
q = 25
d = 10
n = 5
p = 1

for i in range(1, t+1) :
    a=int(input())
    s = []
    cnt = 0
    s.append(a//q)
    cnt = a % q
    s.append(cnt//d)
    cnt = cnt % d 
    s.append(cnt//n)
    cnt = cnt % n
    s.append(cnt)
    print(*s)