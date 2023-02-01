import operator
n,m = map(int,input().split())
s = list(map(int, input().split()))
dict= {}
for i in range(0,n) :
    for j in range(i+1,n) :
        for l in range(j+1,n) :
            p = s[i]+s[j]+s[l]
            if p <= m and p not in dict :
                dict[p] = m-p
dict1 = sorted(dict.items(), key = operator.itemgetter(1))
result = dict1[0][0]
print(result)


