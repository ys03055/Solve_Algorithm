n = int(input())
s = list(map(int,input().split()))
a,b = map(int,input().split())
count = 0

for i in range(len(s)) :
    if s[i] > a :
        s[i] -=a
        count +=1
    else :
        s[i] = 0
        count +=1
for i in range(len(s)) :
    if s[i] >= b :
        count += (s[i] //b)
        s[i] %=b
    else :
        if s[i] !=0 :
            count +=1
            s[i] = 0
        else :
            continue
for i in range(len(s)) :
    if s[i] !=0 :
        count +=1
    else :
        continue

print(count)
