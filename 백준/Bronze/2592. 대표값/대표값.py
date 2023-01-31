import operator

n =10
dict = {}
cnt = 0
for i in range(n) :
    a=int(input())
    cnt +=a
    if a not in dict :
        dict[a] = 1
    else :
        dict[a]+=1
dict1=sorted(dict.items(), key=operator.itemgetter(1), reverse=True)


print(int(cnt/n))
print(dict1[0][0])