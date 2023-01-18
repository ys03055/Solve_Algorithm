t = int(input())
for i in range(1, t+1) :
    a, b = input().split()
    result = ""
    for i in b :
        result+=(i*int(a))
    print(result)