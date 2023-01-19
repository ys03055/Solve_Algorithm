t = int(input())
d = {}
for i in range(1, t+1) :
    a,b = input().split()
    d[a] = b
dic1 = dict(sorted(d.items(),reverse=True))
for j in dic1:
    if dic1[j] == "enter" :
        print(j)
