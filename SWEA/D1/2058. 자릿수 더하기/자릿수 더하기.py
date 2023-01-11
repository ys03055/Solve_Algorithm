n = int(input())
cnt = 0
while n > 0 :
    cnt += n%10
    n = (n- (n%10)) /10
print(int(cnt))