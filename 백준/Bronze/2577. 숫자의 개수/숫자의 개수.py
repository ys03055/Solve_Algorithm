a = int(input())
b = int(input())
c = int(input())
d = a*b*c
d1 = str(d)
x = {}
for i in d1 :
    if i not in x :
        x[i] = 1
    else :
        x[i] +=1
for k in range(0,10) :
    if str(k) not in x :
        x[str(k)] = 0
    else :
        continue
x1 = dict(sorted(x.items()))
for j in x1 :
    print(x1[j])
