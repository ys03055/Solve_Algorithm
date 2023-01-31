s = []
result = []
max_len = 0
for i in range(5) :
    a = list(map(str,input()))
    s.append(a)
    if len(a) > max_len :
        max_len = len(a)
for i in s :
    while True:
        if len(i) != max_len :
            i.append(" ")
        else :
            break
for i in range(max_len):
    for j in range(5) :
        if s[j][i] != " " :
            result.append(s[j][i])
        else :
            continue
for i in (result):
    print(i,end="")