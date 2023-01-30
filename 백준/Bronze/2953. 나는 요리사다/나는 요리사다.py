import sys

n = 5
dict= {}
for i in range(1,n+1) :
    a = list(map(int, sys.stdin.readline().split()))
    dict[i] = sum(a)
print(max(dict, key = dict.get),max(dict.values()))