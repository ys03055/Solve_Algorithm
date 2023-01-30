import sys
n = 4
matrix = []
cnt = 0

for _ in range(101) :
    matrix.append([0 for _ in range(101)])


for i in range(n) :
    a,b,c,d = map(int, sys.stdin.readline().split())
    for i in range(a,c) :
        for j in range(b,d) :
            matrix[i][j]= 1

for x in range(101) :
    for y in range(101) :
        if matrix[x][y] == 1 :
            cnt +=1

print(cnt)