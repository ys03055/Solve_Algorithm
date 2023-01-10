T = int(input())
for i in range(1, T + 1):
    s=list(map(int,input().split()))
    max = 0
    for x in s :
        if x > max :
            max = x
    print(f"#{i} {max}")