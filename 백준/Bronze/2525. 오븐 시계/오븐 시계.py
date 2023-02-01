a,b= map(int, input().split())
time = int(input())
if b + time >= 60 :
    if a+((b+time)/60) >= 24:
        a = (a+((b+time)//60)) %24
        b = (b+time)%60 
    else : 
        a +=((b+time) //60)
        b = (b+time)%60 
else :
    b = b+ time
print(int(a),int(b))