t = int(input())
cnt = 0
result = 0
a = list(map(int, input().split()))
for i in a :
    if i == 1 :
        cnt +=1
        result +=cnt
    else :
        cnt = 0
print(result)