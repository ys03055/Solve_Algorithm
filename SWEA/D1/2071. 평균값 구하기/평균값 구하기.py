T = int(input())
for i in range(1, T + 1):
    s=list(map(int,input().split()))
    p = 0
    avg = 0
    # 총합, 평균값 초기화
    for x in s :
        p +=x
    avg = round(p / len(s))
    print(f"#{i} {avg}")