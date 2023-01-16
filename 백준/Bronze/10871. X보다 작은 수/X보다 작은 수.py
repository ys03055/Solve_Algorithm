a,b = map(int,input().split())
s = list(map(int, input().split()))
l = []
for i in s :
    if i < b :
        l.append(i)
    else :
        continue
for j in l :
    print(j, end=" ")