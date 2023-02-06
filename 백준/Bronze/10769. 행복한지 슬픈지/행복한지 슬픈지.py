t = list(map(str,input()))
l = []
cnt_happy = 0
cnt_sad = 0
for i in t :
    if len(l) == 0  and i == ":" :
        l.append(i)
    elif len(l) == 1 and i == "-" :
        l.append(i)
    elif len(l) == 2 and i == ")" :
        l.clear()
        cnt_happy +=1
    elif len(l) == 2 and i == "(" :
        l.clear()
        cnt_sad +=1
    
if cnt_happy == 0 and cnt_sad == 0:
    print("none")
else:
    if cnt_happy == cnt_sad :
        print("unsure")
    elif cnt_happy > cnt_sad :
        print("happy")
    else :
        print("sad")
