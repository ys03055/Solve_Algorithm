t= 4
s = []
cnt =0
for i in range(t) :
    out_, in_ = map(int,input().split())
    cnt+=in_
    cnt-=out_
    s.append(cnt)
print(max(s))