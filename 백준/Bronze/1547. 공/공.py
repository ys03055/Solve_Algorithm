n = int(input())
ball = 1
for i in range(n) :
    a = list(map(int, input().split()))
    if ball in a :
        a.remove(ball)
        ball = a[0]
print(ball)
