s = list(input())
s1 = s
first = ''.join(s1)
s.reverse()
second = ''.join(s)
if first == second :
    print(1)
else :
    print(0)