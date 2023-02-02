s = []
for i in range(20) :
    a= int(input())
    s.append(a)
w = s[0:10]
k = s[10:20]
w.sort(reverse = True)
k.sort(reverse=True)

w_result = 0
k_result = 0

for x in range(3) :
    w_result +=w[x]
for y in range(3) :
    k_result +=k[y]

print(w_result, k_result)