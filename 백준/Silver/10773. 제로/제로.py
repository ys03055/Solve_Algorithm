n = int(input())
s = []
for i in range(n) :
    a = int(input())
    if a == 0 :
        s.pop()
    else:
        s.append(a)

result = 0    
for i in s:
    result +=i
print(result)