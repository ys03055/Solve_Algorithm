n = int(input())
a = list(map(int, input().split()))
s = []
result = 0
for i in range(n) :
    if a[i] in s :
        result +=1
    else :
        s.append(a[i])
print(result)