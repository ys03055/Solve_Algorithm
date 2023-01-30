t = 102
s= []
for i in range(1, t+1) :
    a= input()
    if a == "문제" :
        s.append(a)
    elif a == "고무오리" and len(s) != 0:
        s.pop()
    elif a == "고무오리" and len(s) == 0:
        s.append('문제')
        s.append('문제')
    elif a == "고무오리 디버깅 끝" :
        break
if len(s) == 0 :
    print("고무오리야 사랑해")
else :
    print('힝구')