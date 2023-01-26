s=[]
for i in range(3) :
    a = int(input())
    s.append(a)

cnt_180 = 0
cnt_s = 0
a = []
for i in range(len(s)) :
    if s[i] in a :
        cnt_s +=1
    a.append(s[i])
    cnt_180 += int(s[i])
if cnt_180 !=180 :
    print("Error")
else :
    if cnt_s+1 == 3 :
        print("Equilateral")
    elif cnt_s+1 == 2:
        print("Isosceles")
    else :
        print("Scalene")