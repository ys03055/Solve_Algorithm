s = list(input())
cnt = 0
result = ""
for i in s :
    if cnt == 10 :
        print(result)
        cnt = 1
        result = i
    else :
        result +=i
        cnt +=1
print(result)