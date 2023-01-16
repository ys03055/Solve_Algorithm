l = []
cnt = 0
for i in range(5) :
    a = int(input())
    if a < 40 :
        a = 40
        l.append(a)
    else :
        l.append(a)
for j in l :
    cnt +=j
print(cnt //5)
