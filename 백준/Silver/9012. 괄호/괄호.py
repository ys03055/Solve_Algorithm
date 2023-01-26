t = int(input())
for i in range(1, t+1) :
    a = input()
    cnt_l = 0
    cnt_r = 0
    s = []
    j = 0
    for i in a :
        if i == "(" :
            cnt_l+=1
            s.append(i)
        elif i == ")" and "(" in s:
            cnt_r +=1
            s.remove("(")
        else :
            print("NO")
            j = 1
            break

    if j != 1 :
        if cnt_l == cnt_r :
            print("YES")
        else :
            print("NO")