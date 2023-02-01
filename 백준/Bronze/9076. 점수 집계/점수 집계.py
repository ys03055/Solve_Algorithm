n = int(input())
for i in range(n) :
    s= list(map(int,input().split()))
    s.sort(reverse=True)
    s.pop(0)
    s.pop(-1)
    cnt = 0
    if s[0] - s[-1] >= 4 :
        print("KIN")
    else :
        for i in s :
            cnt+=i
        print(cnt)
