T = int(input())
result = ""
for i in range(1, T+1) :
    s = list(input())
    s.reverse()
    s1 = ''.join(s)
    l=list(map(str, s1.split()))
    l.reverse()
    l1 = ' '.join(l)
    result =l1
    print(result)