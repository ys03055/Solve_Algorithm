cnt = 0
l = []
for i in range(7) :
    a = int(input())
    if a % 2 == 1 :
        cnt +=a
        l.append(a)
if cnt != 0 :            
    print(cnt)
    print(min(l))
else :
    print(-1)